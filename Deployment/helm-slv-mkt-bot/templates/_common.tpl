{{/*
Common host
*/}}
{{- define "host.templated" -}}
{{- if (.Capabilities.APIVersions.Has "route.openshift.io/v1") }}
{{- print .Chart.Name "-" .Release.Namespace "." .Values.HOST }}
{{- else }}
{{- if and (.Values.ingress.enabled) (eq (.Capabilities.APIVersions.Has "route.openshift.io/v1") false) (eq .Values.ingress.env "prod") }}
{{- print .Chart.Name "." .Values.HOST }}
{{- else }}
{{- print .Chart.Name "-" .Release.Namespace "." .Values.HOST }}
{{- end }}
{{- end }}
{{- end }}
