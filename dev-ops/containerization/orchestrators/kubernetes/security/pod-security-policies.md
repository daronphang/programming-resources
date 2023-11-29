## Security Context

You can enable security settings on a per-Pod basis by setting **security context** attributes in individual Pod YAML files. A security context defines privilege and access control settings for a Pod or Container. However, this approach does not scale.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
    runAsUser: 1000 # 0 for root
    runAsGroup: 3000
    fsGroup: 2000
  volumes:
    - name: sec-ctx-vol
      emptyDir: {}
  containers:
    - name: sec-ctx-demo
      image: busybox:1.28
      command: ["sh", "-c", "sleep 1h"]
      volumeMounts:
        - name: sec-ctx-vol
          mountPath: /data/demo
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          add: ["NET_ADMIN", "SYS_TIME"] # only applicable at container level
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-pod
spec:
  securityContext:
    runAsUser: 1001
  containers:
    - image: ubuntu
      name: web
      command: ["sleep", "5000"]
      securityContext:
        runAsUser: 1002 # overriding 1001

    - image: ubuntu
      name: sidecar
      command: ["sleep", "5000"]
```

## Pod Security Policies

Pod Security Policies allows you to define security settings at the cluster level. You can then apply them to target sets of Pods as part of the deployment process.

Pod Security Policies are implemented as an admission controller, and in order to use them, a Pod's ServiceAccount must be authorized to use it.

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
    name: restricted
annotations:
    seccomp.security.alpha.kubernetes.io/allowedProfileNames: 'docker/default' apparmor.security.beta.kubernetes.io/allowedProfileNames: 'runtime/default' seccomp.security.alpha.kubernetes.io/defaultProfileName: 'docker/default'
    apparmor.security.beta.kubernetes.io/defaultProfileName: 'runtime/default'
spec:
    privileged: false
    allowPrivilegeEscalation: false # Prevent privilege escalation
    requiredDropCapabilities:
        - ALL # Drops all root capabilities (non-privileged user)
    # Allow core volume types.
    volumes:
        - 'configMap'
        - 'emptyDir'
        - 'projected'
        - 'secret'
        - 'downwardAPI'
        - 'persistentVolumeClaim'
    hostNetwork: false # Prevent access to the host network namespace
    hostIPC: false # Prevent access to the host IPC namespce
    hostPID: false # Prevent access to the host PID namespace
    runAsUser:
        rule: 'MustRunAsNonRoot' # Prevent from running as root
    runAsGroup:
        rule: 'MustRunAs' # controls which primary Group ID containers are run with
    ranges:
        - min: 1
          max: 65535
    seLinux:
        rule: 'RunAsAny' # Any SELinux options can be used
    supplementalGroups:
        rule: 'MustRunAs'  # Allow all except root (UID 0)
        ranges:
            - min: 1
              max: 65535
    fsGroup:
        rule: 'MustRunAs'  # Sets range for groups that own Pod volumes
        ranges:
            - min: 1
              max: 65535
    readOnlyRootFilesystem: true # Force root filesystem to be R/O
    forbiddenSysctls:
        - '*' #Forbids any sysctls from being accessible from a pod
```
