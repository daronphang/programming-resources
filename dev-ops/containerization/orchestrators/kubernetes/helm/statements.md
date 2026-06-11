## Context

The dot represents the current scope or context.

```yaml
# values.yaml
image:
  repository: nginx
  tag: "1.21"

# template.yaml
{{- with .Values.image }}
  repository: {{ .repository }}  # Notice: No ".Values.image" needed!
  tag: {{ .tag }}                # The dot is NOW .Values.image
{{- end }}
```

## Conditional (if, with, range)

Every conditional must have a corresponding `{{ end }}`. Otherwise, a parsing error will be thrown.

```yaml
{{- if .Values.loadGenerator.enabled }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: load-generator
...
{{- end }}
```

```yaml
{{- range .Values.items }}
- name: {{ . }}
{{- end }}
```

```yaml
{{- with .Values.metadata }}
  app: {{ .name }}
{{- end }}
```

## Include

When using include, you always see a dot at the end. This is because the helper template is like a separate function. It has no data unless you explicitly hand it the dot. By passing the dot, you are giving that helper permission to see all your values and variables.

```yaml
{ { include "mychart.labels" . } }
```

## Loops

```yaml
{{- range $p, $vp := $.Values.platform }}
{{- range $n, $vn := . }}
```

## Piping

```yaml
resources:
{ { - .resources | toYaml | nindent 12 } }
```

## Silent assignment

This ensures the result isn't printed directly into your YAML file. It just does the work in the background. Also, silent assignment is necessary for set function as it is designed to return the entire object that was just modified, which messes up your final Kubernetes YAML.

```yaml
{ { - $_ := set . "application" $.Chart.Name } }
```

## Keywords

### nindent

Stands for newline and indent. The default rule for indents is to follow "parent + 2" rule, where every nesting level is 2 spaces.
