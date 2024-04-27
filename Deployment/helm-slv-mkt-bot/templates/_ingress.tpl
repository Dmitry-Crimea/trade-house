{{/*
Create ingress
*/}}t
{{- define "ingress.template" }}
kind: Ingress
apiVersion: networking.k8s.io/v1
metadata:
  name: {{ .Chart.Name }}
  labels:
    app: {{ .Chart.Name }}
    name: {{ .Chart.Name }}
spec:
  rules:
    - host: {{ template "host.templated" . }}
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: {{ template "istio-port-name.templated" . }}
                port:
                  number: {{ template "istio-port.templated" . }}
{{- end }}
