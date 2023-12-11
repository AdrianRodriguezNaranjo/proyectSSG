# Proyecto de SSG
## Tarea a realizar:
Crea una base de datos nueva en tu instalación de Odoo.

Se pretende crear una aplicación personalizada que sirva de apoyo a una empresa de desarrollo de software,
de la que vamos a ir explicando en este documento cuál es su operativa diaria.

### Entidades: Incluyen consultas, altas, bajas y modificaciones.
* Empresas-contratadoras: Que encargan proyectos a la empresa.
* Proyectos: Aplicaciones informáticas
* Tareas: Acciones que un jefe de proyectos considera necesarias para realizar un proyecto concreto.
* Subtareas: Acciones que un analista considera necesarias para realizar una tarea.

### Roles de los usuarios:

* Administrador:
Es el desarrollador de la aplicación. Tiene permiso para todo.
Este perfil no opera en la gestión diaria de la empresa.
Sólo tiene una función de ajuste y parametrización de la aplicación de gestión.

* Jefe de proyectos:
Crean empresas-contratadoras. CRUD
Crean proyectos. CRUD
Crean tareas dentro de los proyectos que asignan a los analistas. CRUD
Pueden modificar proyectos y tareas, aunque no hayan sido creados por ellos        

* Analista:
Sólo consultan empresas-contratadoras.
Sólo consultan proyectos.
Crean tareas dentro de los proyectos que asignan a los programadores. CRUD

* Programador:
Pueden modificar las tareas. No pueden crearlas ni eliminarlas.       

### Operativa:

Los Empresas contratadoras encargan Proyectos a nuestra empresa, que son organizados, analizados y finalmente programados por el personal de la empresa.

Cada proyecto que nos encarguen implica la creación de 1 proyecto en nuestra aplicación.

Implementa una aplicación personalizada para la gestión de proyectos, que utilice el módulo “Proyecto” ya existente en Odoo como base, 
para utilizarla en la gestión de proyectos de nuestra empresa de desarrollo de software en particular. 

En nuestra aplicación deben poderse realizar todas las operaciones que se describen en cada uno de los roles de usuario indicados arriba.

El formulario asociado al CRUD de empresas contratadoras, debe incluir un listado de todos los proyectos que esa empresa nos ha contratado, 
desde el cual se debe poder acceder a la consulta y modificación de cada uno de ellos (los proyectos).­

Todo debe conseguirse creando un nuevo módulo de Odoo, que se instalará de forma independiente, 
y que debe incluir todo lo necesario para modificar la funcionalidad de otros módulos o aspectos base de Odoo si así se considera, 
para conseguir el objetivo que se pide.
