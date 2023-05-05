from enum import Enum
from abc import ABC, abstractmethod


class SagaError(Exception):
    pass


class Metadata:
    taskname = None
    task = None
    success_state = None
    failed_state = None
    args = None


class SagaStateOrchestrator(ABC):
    '''
    Saga orchestrator implemented as a state machine.

    Takes in states as an argument of type Enum, and requires
    START and END states to be defined.

    Current state is updated in memory and not in persistent storage.

    If a particular task depends on the return value of a previous task,
    the return value must be of tuple.
    '''
    def __init__(self, states: Enum):
        if not isinstance(states, Enum):
            raise ValueError('states must be of Enum class')
        if 'START' not in states.__members__:
            raise ValueError('START must be defined in states')
        elif 'END' not in states.__members__:
            raise ValueError('END must be defined in states')
        self.saga_logs = []
        self.STATES = states
        self.tasks_hash = {}
        self._current_state = states.START
        self.return_value = ()
    
    def add_sync_task(self, task: Metadata):
        self.tasks_hash[task.state] = task

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, v: Enum):
        self._current_state = v
    
    @abstractmethod
    def transit_state(self):
        # to override with client's class
        # transiting to END state MUST be defined; else
        # flow will be in a continous loop
        if self.current_state == self.STATES.START:
            self.current_state = self.STATES.DEDUCT_QUOTA
        elif self.current_state == self.STATES.DEDUCT_QUOTA:
            self.current_state = self.STATES.REMOVE_SFF
            self.tasks_hash[self.STATES.ROLLBACK_QUOTA].args = self.return_value
        elif self.current_state == self.STATES.REMOVE_SFF:
            self.current_state = self.STATES.END 
    
    def perform_precheck(self):
        # check if all states have tasks defined
        for state in self.STATES:
            if state.name not in self.tasks_hash:
                raise ValueError(f'{state.name} must have a task defined')

    def execute_task(self):
        task = self.tasks_hash[self.current_state]
        try:
            rv = task.callable(*task.args)
            if isinstance(rv, tuple):
                self.return_value = rv
            else:
                self.return_value = ()
            self.saga_logs.append(f'executed {self.current_state.name} success')
            self.current_state = task.success_state
        except Exception as exc:
            self.saga_logs.append(f'failed to execute {self.current_state}')
            self.current_state = task.failed_state
    
    def execute(self):
        self.perform_precheck()
        while True:
            if self.current_state == self.STATES.START:
                self.saga_logs.append('starting saga orchestrator workflow')
            if not self.current_state or self.current_state == self.STATES.END:
                self.saga_logs.append('saga orchestrator workflow completed')
                break
            self.transit_state()
            self.execute_task()
            
            


        
