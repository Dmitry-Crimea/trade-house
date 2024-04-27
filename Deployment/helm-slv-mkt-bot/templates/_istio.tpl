{{/*
Create templated istio-port-name
*/}}
{{- define "istio-port-name.templated" -}}
{{- print .Chart.Name }}
{{- end }}

{{/*
Create templated istio-port
*/}}
{{- define "istio-port.templated" -}}
{{- print .Values.APP_PORT }}
{{- end }}

{{/*
Create templated istio-port
*/}}
{{- define "route-port.templated" -}}
{{- print .Values.APP_PORT }}
{{- end }}
