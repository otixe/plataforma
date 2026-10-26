# Pi · runtime de ejecución

## Qué es / qué resuelve

Pi es el runtime extensible del agente: ciclo de conversación con modelos, ejecución de tools, sesiones duraderas y UI de terminal. La plataforma lo usa como base de ejecución en vez de pedir al servicio de memoria que ejecute trabajos arbitrarios. Existe un fork de Otixe: debe distinguirse del upstream y de las extensiones publicadas por separado.

## Internos y tecnologías

Node.js/TypeScript aloja extensiones y tools. Una extensión registra tools, comandos y hooks de ciclo de vida. Skills Markdown aportan instrucciones para tareas específicas. Historia de sesión y compactación sostienen trabajo largo, pero no reemplazan un tablero compartido. Modelos y proveedores se configuran independientemente de Cerebro.

Codemode ejecuta JavaScript en QuickJS: sin globals directos de Node, filesystem, red ni timers. Los scripts usan tools registradas para operaciones externas y emiten resultados seleccionados mediante `text`, `console.log` o `return`. Esto permite filtrar un resultado grande antes de enviarlo al modelo; no aísla los permisos de las tools subyacentes.

## Quickstart: runtime público

Requisitos: Node.js **22.19+** y un proveedor/cuenta que tengas autorización para usar. Revisá antes el paquete upstream y su política de confianza.

```sh
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pi --version
pi
```

Completá login/configuración del proveedor elegido desde la terminal; no guardes secretos en Git ni en documentación. Instalar el runtime **no** instala Cerebro, provisiona identidad ni crea oficinas. Para comportamiento del fork y API de extensiones compatible, consultá el [repo Pi](https://github.com/otixe/pi).

## Quickstart: una extensión

```sh
pi install npm:@otixe/pi-oficinas@0.1.0
```

Configurá un equipo y abrí un **proceso Pi nuevo**. Leé [Oficinas](oficinas.md) antes de delegar. AMA requiere específicamente exposición/codemode compatibles —validado contra Pi 1.4.0—; instalar un paquete no demuestra que sus entry points cargaron.

## Seguridad y aceptación

- Confiá explícitamente en el código instalado: tiene permisos de sistema del proceso.
- Verificá versión de runtime, lista de tools activas e identidad propia tras configurar.
- Un install exitoso no prueba servicio funcional ni autorización de acciones.
- Hacé explícitas la política de datos del modelo externo y los permisos de tools locales.

Fuentes: [README upstream](https://github.com/earendil-works/pi), [monorepo de extensiones](https://github.com/otixe/pi-oficinas), [registro de fuentes](sources.md).
