# Oficinas · equipos persistentes

## Qué es / qué resuelve

Una oficina es un espacio persistente de agente con rol acotado: configuración, tools autorizadas y referencias de trabajo sobreviven a cada conversación. Un coordinador asigna, especialistas ejecutan sus tareas y revisores comprueban aceptación de manera independiente. Un ayudante transitorio no es una oficina persistente ni debería heredar poderes administrativos.

## Internos y tecnologías

La extensión Pi está escrita en TypeScript, con configuración explícita JSON y fichas/skills Markdown. Un mapa de equipo versión 2 declara roles, espacios y fuentes de keys de identidad. La configuración es validada y controlada por su dueño; ningún ejemplo contiene una key real. Estado de tareas y correspondencia viven en Cerebro, no sólo en panes locales.

La interfaz de agentes delegados es asíncrona: asignar alcance acotado, seguir resultados y conservar al responsable. Un pane visible o una notificación no autoriza a saltarse tablero, confianza ni gate de revisión.

## Quickstart: paquete publicado, equipo configurado

Requisitos: runtime Pi compatible, código confiable, definición de equipo administrada por el operador y —para trabajo compartido— identidad Cerebro provisionada. Partí del ejemplo del paquete, no de un schema inventado.

```sh
git clone https://github.com/otixe/pi-oficinas.git
cd pi-oficinas
pi install npm:@otixe/pi-oficinas@0.1.0
```

1. Adaptá [ejemplo de equipo e instrucciones](https://github.com/otixe/pi-oficinas/tree/main/packages/pi-oficinas) a tus espacios y roles autorizados.
2. Definí `PI_OFICINAS_EQUIPO` con la configuración validada versión 2; provisioná la key propia de cada agente fuera del código. Limitá la escritura de configuración a su dueño.
3. Abrí un proceso Pi nuevo en el espacio elegido. Verificá identidad, tools permitidas y atribución del servidor.
4. Probá una tarea reversible: leer → tomar → evidencia → entregar → revisión independiente. No uses publicación ni producción como primer test.

## La familia de extensiones

| Paquete npm | Foco |
| --- | --- |
| `@otixe/pi-oficinas` | Coordinación de equipo/oficinas. |
| `@otixe/pi-plan-gate` | Plan de trabajo y gates. |
| `@otixe/pi-renovacion` | Flujo de continuidad/renovación. |
| `@otixe/pi-cache-estable` | Estabilidad de prompt/caché. |
| `@otixe/pi-herramientas` | Integración de catálogo/activación de tools. |
| `@otixe/pi-cerebro-ama` | Bridge Cerebro más perfiles AMA. |

Los seis tienen metadatos públicos de registro en `0.1.0`. **No** se recomienda cargar los seis a ciegas: AMA reemplaza el bridge Cerebro y el activador de herramientas; evitá entry points duplicados. Consultá [configuración AMA](ama.md) para compatibilidad y rollback.

## Aceptación y límites

Probá una operación denegada además de una permitida. Un especialista no debe aprobar su entrega de alto impacto sólo porque tenga visible una tool de revisión. Persistencia requiere backups, verificación del estado actual y evidencia conservada; dejar una terminal abierta no alcanza.
