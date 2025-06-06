La solución implementa un editor de texto enriquecido con funcionalidad de control de versiones, basada en una estructura de datos de lista doblemente enlazada. Cada nodo de esta lista encapsula un estado del documento, permitiendo una navegación eficiente tanto hacia versiones anteriores (función de undo) como hacia versiones posteriores (función de redo).

El historial se gestiona mediante un puntero dinámico al nodo actual (current_node), y cualquier nueva edición registrada en un punto intermedio del historial elimina los nodos siguientes, garantizando la consistencia del estado.

La interfaz gráfica se construyó utilizando el módulo tkinter, con componentes visuales estilizados mediante la biblioteca ttkbootstrap, facilitando una experiencia de usuario moderna y responsiva. El usuario puede interactuar con el historial mediante botones que invocan operaciones sobre la lista enlazada, permitiendo así la gestión temporal del contenido textual.
