# Fuentes y estado

**Fecha de documentación: 2026-10-25.** Disponible no significa listo para producción. Este registro separa publicación, arquitectura reportada y evidencia medida.

## Fuentes públicas

| Fuente | Qué respalda | Condición |
| --- | --- | --- |
| [Pi upstream](https://github.com/earendil-works/pi) y [fork de Otixe](https://github.com/otixe/pi) | Runtime, ciclo de paquetes/extensiones, codemode y seguridad. | Docs locales de runtime 1.4.0; versiones futuras pueden diferir. |
| [pi-oficinas](https://github.com/otixe/pi-oficinas) | Equipo, resolución de identidad y familia de extensiones. | Revisión inspeccionada: `8bb092653cefa886165cf4588c1d6bc43fd14b95`. |
| [README AMA](https://github.com/otixe/pi-oficinas/tree/main/packages/pi-cerebro-ama) | Perfiles 8/14, configuración, compatibilidad, medición y rollback. | Adaptador para Cerebro existente; no incluye servidor. |
| [Script de medición AMA](https://github.com/otixe/pi-oficinas/blob/main/packages/pi-cerebro-ama/bin/measure-jsonl.py) | Cálculo offline de uso y particiones. | Metadatos registrados, no facturas ni causalidad. |
| Registro npm `@otixe/*` | Seis versiones de paquetes en `0.1.0`. | Metadatos verificados; esta entrega no prueba todos los installs de registro. |
| [Fork Hermes](https://github.com/otixe/hermes-agent) | Trabajo relacionado en runtimes de agentes. | No se presenta como uno de los cuatro componentes. |

Parte de la prosa de paquetes es anterior a publicar y todavía describe artefactos locales. Para disponibilidad prevalece el registro vivo; las advertencias de compatibilidad siguen vigentes.

## Fuentes internas resumidas de forma segura

Plan de arquitectura y guía maestra de Cerebro respaldan gateway, almacenamiento, búsqueda, tareas y RBAC. Harness v5 respalda separación de poderes, gates proporcionales y evidencia duradera. Un runbook de rediseño UI/despliegue de Sinapsis respalda el stack **reportado** frontend React/Vite + BFF FastAPI (backend para frontend), cliente de Cerebro. El coordinador confirmó arquitectura y publicación pendiente.

Los documentos privados **no se incluyen ni enlazan a endpoints privados**. No equivalen a distribución pública de servidor ni a instalador Sinapsis reproducible. No se exportan logs raw, documentos personales de agentes ni settings privados. Las instrucciones de publicación de esos componentes siguen pendientes.

## AMA y resultados cuantificados

Este manual **no lleva cifras de ahorro**. AMA se presenta como diseño —el patrón de código contra una API tipada aplicado a Cerebro— y su eficiencia se verifica en tu propia carga. Los resultados cuantificados se agregarán después de una medición representativa y reproducible. Los perfiles 8/14 salen del README del paquete y de un censo de uso real de tools; no se afirma ninguna medición de ahorro del perfil líder.

## Requisitos antes de publicar

1. QA independiente de hechos, traducciones, diagramas, enlaces y datos privados.
2. El responsable crea/revisa `otixe/otixe` y `otixe/plataforma`: son destinos propuestos, no repos activos verificados en esta fecha.
3. Publicar perfil; configurar Pages (Actions), protección de entorno y aprobar manualmente despliegue documental.
4. Reemplazar pendientes/enlaces sólo cuando existan releases Cerebro/Sinapsis y pase su QA de instalación.

Build estricto y cero hallazgos de escáner son evidencia, no prueba de verdad de cada afirmación ni de eliminación de todo dato privado. La revisión humana sigue formando parte de la aceptación.
