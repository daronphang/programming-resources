## Implementations

### Grouping by directories

```go
// project/node/node.go
type NodeClient interface {
	CreateNode() error
	GetNode() error
}

type NodeService struct {
	httpClient http.Client
}

func New(httpClient *http.Client) *NodeService {
	return &NodeService{httpClient: *httpClient}
}

func (s *NodeService) CreateNode() error {
	return nil
}

func (s *NodeService) GetNode() error {
	return nil
}

```

```go
// project/resource/resource.go
type ResClient interface {
	CreateResource() error
	GetResource() error
}

type ResourceService struct {
	httpClient http.Client
}

func New(httpClient *http.Client) *ResourceService {
	return &ResourceService{httpClient: *httpClient}
}

func (s *ResourceService) CreateResource() error {
	return nil
}

func (s *ResourceService) GetResource() error {
	return nil
}

```

```go
// main.go
type Client interface {
	node.NodeClient
	resource.ResClient
}

type Service struct {
	node.NodeClient
	resource.ResClient
}

func New() Client {
	httpClient := &http.Client{}
    // Actual implementation
	return &Service{
		NodeClient: node.New(httpClient),
		ResClient:  resource.New(httpClient),
	}
}
```
