# Born2beRoot — Debian 13 + LibreSpeed

<div align="center">

![Debian](https://img.shields.io/badge/Debian-13-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![VirtualBox](https://img.shields.io/badge/VirtualBox-Hypervisor-183693?style=for-the-badge&logo=virtualbox&logoColor=white)
![Lighttpd](https://img.shields.io/badge/Lighttpd-Webserver-007ACC?style=for-the-badge&logo=lighttpd&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-Backend-777BB4?style=for-the-badge&logo=php&logoColor=white)
![UFW](https://img.shields.io/badge/UFW-Firewall-43853D?style=for-the-badge&logo=linux&logoColor=white)

*A rigorous system administration project from the 42 Network, focusing on secure server deployment, virtualization, and web services.*

</div>

---

## 📚 Índice
1. [Creación de la máquina virtual](#1-creación-de-la-máquina-virtual)
2. [Instalación de Debian](#2-instalación-de-debian)
3. [Particionado y LVM](#3-particionado-y-lvm)
4. [Configuración del hostname](#4-configuración-del-hostname)
5. [Usuarios y grupos](#5-usuarios-y-grupos)
6. [Política de contraseñas](#6-política-de-contraseñas)
7. [Configuración de sudo](#7-configuración-de-sudo)
8. [Configuración de SSH](#8-configuración-de-ssh)
9. [Firewall UFW](#9-firewall-ufw)
10. [AppArmor](#10-apparmor)
11. [Script de monitoring](#11-script-de-monitoring)
12. [Cron](#12-cron)
13. [LibreSpeed](#13-librespeed)
14. [Lighttpd](#14-lighttpd)
15. [PHP](#15-php)
16. [Instalación de LibreSpeed](#16-instalación-de-librespeed)
17. [Configuración de VirtualBox](#17-configuración-de-virtualbox)
18. [Comprobaciones](#18-comprobaciones)
19. [Problemas encontrados y soluciones](#19-problemas-encontrados-y-soluciones)
20. [Comandos útiles para la defensa](#20-comandos-útiles-para-la-defensa)
21. [Checklist](#21-checklist)
- [Fuentes](#-fuentes)
- [Conclusión](#-conclusión)

---

## 🚀 Introducción

**Born2beRoot** es un proyecto de administración de sistemas de la red 42 cuyo objetivo es crear y configurar una máquina virtual con un sistema operativo GNU/Linux, aplicando estrictas medidas de seguridad, control de acceso y gestión de recursos.

En este proyecto se utiliza:
- **VirtualBox** como hipervisor de virtualización.
- **Debian 13** como sistema operativo base.
- **LVM (Logical Volume Manager)** para la gestión avanzada del almacenamiento.
- **OpenSSH** para la administración remota segura.
- **UFW (Uncomplicated Firewall)** como cortafuegos del sistema.
- **AppArmor** como sistema de control de acceso obligatorio (MAC).
- **sudo** con políticas estrictas de seguridad y registro de auditoría.
- Un script Bash de monitorización ejecutado de forma automatizada mediante **cron**.
- **Lighttpd** como servidor web ligero.
- **PHP** para ejecutar el backend de la aplicación adicional.
- **LibreSpeed** como servicio adicional autoalojado para realizar pruebas de velocidad de red.

### Arquitectura General del Servidor

```text
                        HOST
                         │
                    VirtualBox
                         │
                 ┌───────┴───────┐
                 │                │
              SSH :4241        HTTP :80
                 │                │
                 ▼                ▼
          ┌─────────────────────────────┐
          │        Debian 13 VM         │
          │                             │
          │  SSH                        │
          │  UFW                        │
          │  AppArmor                   │
          │  LVM                        │
          │                             │
          │  Lighttpd                   │
          │      │                      │
          │      └── LibreSpeed         │
          │                             │
          │  monitoring.sh + cron       │
          └─────────────────────────────┘
```

> ⚠️️ **Nota:** El *subject* oficial de Born2beRoot es siempre la referencia principal para los requisitos de evaluación. Las guías y documentación complementaria se utilizan como apoyo técnico.

---

## 🎯 Objetivos

Los principales propósitos del proyecto son:
- Comprender en profundidad el funcionamiento y la arquitectura de una máquina virtual.
- Instalar, configurar y administrar un servidor Debian puro **sin interfaz gráfica**.
- Utilizar LVM para estructurar y gestionar volúmenes de almacenamiento flexibles.
- Crear y administrar usuarios y grupos siguiendo convenciones estrictas.
- Aplicar políticas robustas de contraseñas y caducidad.
- Configurar `sudo` con restricciones de seguridad avanzadas.
- Establecer conexiones SSH seguras en un puerto no estándar.
- Desplegar y configurar un firewall restrictivo con UFW.
- Verificar y habilitar perfiles de seguridad con AppArmor.
- Desarrollar un script automatizado de monitorización de recursos del sistema.
- Automatizar tareas del sistema operativo mediante `cron`.
- Desplegar un servicio web adicional útil (**LibreSpeed**) empleando tecnologías web modernas y livianas como Lighttpd y PHP.

---

## 🛠️️ Tecnologías Utilizadas

| Tecnología | Propósito / Uso |
| :--- | :--- |
| **VirtualBox** | Hipervisor de virtualización por hardware |
| **Debian 13** | Distribución GNU/Linux base del servidor |
| **LVM** | Gestión abstracta de discos y volúmenes lógicos |
| **OpenSSH** | Protocolo y servidor de acceso remoto cifrado |
| **UFW** | Interfaz simplificada de gestión de iptables (Firewall) |
| **AppArmor** | Módulo de seguridad de control de acceso obligatorio |
| **sudo** | Ejecución de comandos con privilegios elevados |
| **Bash** | Lenguaje de scripting para monitorización de hardware |
| **cron** | Planificador de tareas automatizadas del sistema |
| **Lighttpd** | Servidor web HTTP optimizado para recursos ligeros |
| **PHP** | Lenguaje interpretado para procesar el backend de LibreSpeed |
| **LibreSpeed** | Aplicación web de test de velocidad autoalojada |

---

## 1. Creación de la máquina virtual

La máquina virtual se configura y crea empleando VirtualBox de acuerdo con los parámetros especificados:

| Parámetro | Valor de Configuración |
| :--- | :--- |
| **Nombre** | `born2beroot` |
| **Tipo de OS** | Linux |
| **Versión** | Debian (64-bit) |
| **Memoria RAM** | Mínimo 1 GB (ampliable según servicio adicional) |
| **Disco Duro** | VDI (VirtualBox Disk Image) |
| **Almacenamiento** | Dinámicamente asignado |
| **Interfaz Gráfica** | Desactivada (Headless / Modo Texto puro) |

> 💡 **Consejo:** Para ejecutar correctamente servicios adicionales como LibreSpeed, se recomienda asignar recursos de RAM y almacenamiento ligeramente superiores al mínimo estricto del proyecto. Asegúrese de guardar el archivo de disco en una partición con suficiente capacidad libre.

---

## 2. Instalación de Debian

La instalación de Debian se realiza mediante el asistente en modo texto, omitiendo por completo cualquier entorno de escritorio para garantizar un entorno de servidor limpio, ligero y seguro.

Durante el proceso se definen:
- Selección de idioma, ubicación geográfica y distribución de teclado.
- Asignación del **Hostname** oficial del sistema.
- Creación de la cuenta de usuario principal y credenciales de root.
- Esquema de particionado asistido mediante **LVM**.
- Selección de paquetes de software básicos (utilidades estándar del sistema y servidor SSH).

---

## 3. Particionado y LVM

El Logical Volume Manager (**LVM**) permite abstraer los dispositivos de almacenamiento físico en capas lógicas dinámicas, facilitando la gestión de tamaños sin necesidad de reasignar particiones físicas estáticas.

### Estructura Conceptual de LVM
```text
Disco físico (sda)
    │
    ▼
Partición principal
    │
    ▼
Physical Volume (PV)
    │
    ▼
Volume Group (VG)
    │
    ├── root (/)
    ├── swap (Intercambio)
    ├── home (/home)
    ├── var (/var)
    ├── srv (/srv)
    ├── tmp (/tmp)
    └── var-log (/var/log)
```

### Comprobación del Almacenamiento
Para verificar el estado de los volúmenes lógicos y el uso de espacio en disco, se emplean los siguientes comandos:
```bash
lsblk
sudo pvs
sudo vgs
sudo lvs
df -h
```

---

## 4. Configuración del Hostname

El nombre de host del sistema debe seguir estrictamente la nomenclatura requerida por el proyecto (`<login>42`).

- **Hostname asignado en este proyecto:** `dcasasol42`

Para verificar el hostname actual:
```bash
hostnamectl
```

Para modificarlo en caliente:
```bash
sudo hostnamectl set-hostname dcasasol42
```

Asimismo, se verifica la correspondencia en el archivo de resolución local `/etc/hosts`:
```bash
cat /etc/hosts
```
Debe existir una entrada vinculando la dirección de bucle local (`127.0.0.1`) con el hostname asignado.

---

## 5. Usuarios y grupos

El usuario principal debe pertenecer obligatoriamente a los grupos de administración y control definidos en las pautas de evaluación.

### Jerarquía de Grupos del Usuario Principal
`dcasasol42`
├── `sudo` (Privilegios administrativos)
└── `user42` (Grupo específico requerido por el subject)

Para comprobar los grupos asignados a un usuario:
```bash
groups dcasasol42
getent group sudo
getent group user42
```

Para añadir un usuario a los grupos correspondientes:
```bash
sudo usermod -aG sudo dcasasol42
sudo usermod -aG user42 dcasasol42
```
> 🔄 **Nota:** Tras modificar la pertenencia a grupos de una sesión activa, es obligatorio cerrar sesión y volver a iniciarla para que el kernel aplique los cambios de credenciales.

---

## 6. Política de contraseñas

Para garantizar la seguridad de las claves de acceso, se implementa el paquete `libpam-pwquality`, el cual audita la complejidad de las contraseñas según reglas avanzadas.

### Instalación de la librería
```bash
sudo apt install libpam-pwquality
```

### Configuración en PAM (`/etc/pam.d/common-password`)
Ejemplo de directivas aplicadas:
```text
minlen=10
ucredit=-1
dcredit=-1
maxrepeat=3
reject_username
difok=7
enforce_for_root
```
* **Longitud mínima:** Mínimo de 10 caracteres.
* **Mayúsculas y números:** Obligación de incluir al menos una letra mayúscula y un número (`ucredit=-1`, `dcredit=-1`).
* **Caracteres repetidos:** Restricción máxima de 3 caracteres idénticos consecutivos.
* **Nombre de usuario:** Rechazo automático si contiene el nombre de la cuenta.
* **Historial de cambios:** Exigencia de que al menos 7 caracteres sean diferentes respecto a la clave anterior (`difok=7`).
* **Aplicación en root:** Extensión de la política al superusuario (`enforce_for_root`).

### Caducidad de Contraseñas (`/etc/login.defs`)
Se establecen políticas temporales de expiración:
```text
PASS_MAX_DAYS 30
PASS_MIN_DAYS 2
PASS_WARN_AGE 7
```

Para verificar las políticas de caducidad de un usuario o del superusuario:
```bash
sudo chage -l dcasasol42
sudo chage -l root
```

---

## 7. Configuración de sudo

El usuario administrador opera mediante el comando `sudo`. Para comprobar que la elevación de privilegios funciona correctamente:
```bash
sudo whoami
```
*Resultado esperado:* `root`

### Parámetros de Seguridad en Sudoers
La personalización de sudo se gestiona mediante el comando de edición segura:
```bash
sudo visudo
```
Se pueden aplicar directivas adicionales de seguridad, tales como:
```text
Defaults passwd_tries=3
Defaults logfile="/var/log/sudo/sudo.log"
```

Para auditar y consultar los comandos ejecutados a través de sudo en los registros del sistema:
```bash
sudo journalctl _COMM=sudo
```

---

## 8. Configuración de SSH

El servicio Secure Shell (**SSH**) permite la administración remota cifrada de la máquina virtual.

### Instalación del Servidor SSH
```bash
sudo apt install openssh-server
```

### Configuración Principal (`/etc/ssh/sshd_config`)
* **Puerto de escucha:** Configurado en el puerto `4241` (Nota: Si el subject exige estrictamente el puerto `4242`, modifíquese acorde en este archivo, el firewall y VirtualBox).
* **Acceso de Root:** Desactivación estricta de conexiones directas para el superusuario:
  ```text
  PermitRootLogin no
  Port 4241
  ```

### Verificación y Gestión del Servicio
```bash
sudo sshd -t
sudo systemctl restart ssh
sudo systemctl status ssh
```

Para conectarse de forma remota desde el sistema host:
```bash
ssh dcasasol42@localhost -p 4241
```

---

## 9. Firewall UFW

UFW proporciona una interfaz amigable para controlar las reglas de filtrado de paquetes del kernel.

### Instalación y Activación
```bash
sudo apt install ufw
sudo ufw enable
```

### Reglas de Puertos Permitidos
Se abren únicamente los puertos estrictamente necesarios para la administración remota y el servicio web:
```bash
sudo ufw allow 4241
sudo ufw allow 80
```

### Comprobación del Estado del Firewall
```bash
sudo ufw status verbose
```
*Ejemplo de salida esperada:*
```text
Status: active
To                         Action      From
--                         ------      ----
4241                       ALLOW       Anywhere
80                         ALLOW       Anywhere
```
> ⚠️ *Nota:* Si el subject exige el puerto `4242` para SSH, asegúrese de reemplazar `4241` en las reglas correspondientes.

---

## 10. AppArmor

AppArmor es un módulo de seguridad de Control de Acceso Obligatorio (MAC) que confina los programas a perfiles de seguridad específicos, limitando sus privilegios operativos en el sistema de archivos.

### Comprobación de Estado y Servicio
```bash
sudo aa-status
sudo systemctl status apparmor
```

Si el servicio se encontrase inactivo por cualquier motivo, se habilita e inicia con:
```bash
sudo systemctl enable apparmor
sudo systemctl start apparmor
```

---

## 11. Script de monitoring

El proyecto exige un script en Bash encargado de recopilar estadísticas vitales del sistema y transmitirlas en tiempo real a todas las terminales activas mediante el comando `wall`.

### Ubicación del Script
El script se sitúa comúnmente en:
```text
/usr/local/bin/monitoring.sh
```
Debe comenzar estrictamente con el shebang reglamentario:
```bash
#!/bin/bash
```

### Métricas Recopiladas por el Script
1. **Arquitectura del sistema operativo** y versión del kernel.
2. **Número de CPUs físicas** instaladas.
3. **Número de CPUs virtuales** (vCPUs).
4. **Memoria RAM utilizada** y porcentaje de ocupación actual.
5. **Espacio de almacenamiento en disco** utilizado y porcentaje global.
6. **Carga actual de la CPU** expresada en porcentaje.
7. **Fecha y hora del último reinicio** del sistema.
8. **Estado actual de LVM** (Activo / Inactivo).
9. **Número de conexiones TCP** establecidas activas.
10. **Número de usuarios únicos** conectados al sistema.
11. **Dirección IP** de la máquina e interfaz de red.
12. **Dirección MAC** de la interfaz física.
13. **Número total de comandos ejecutados** mediante `sudo`.

### Ejecución Manual y Transmisión
Para probar la ejecución manual del script con privilegios de superusuario:
```bash
sudo bash /usr/local/bin/monitoring.sh
```
El comando `wall` difunde el mensaje generado de manera simultánea a todas las terminales registradas de los usuarios conectados. Para inspeccionar las sesiones activas del sistema:
```bash
who
users
loginctl list-sessions
```

---

## 12. Cron

El planificador de tareas del sistema (`cron`) se encarga de ejecutar de forma automática el script de monitorización a intervalos regulares de 10 minutos.

### Configuración del Crontab de Root
Se edita el crontab del superusuario:
```bash
sudo crontab -e
```
Añadiendo la siguiente regla de planificación:
```cron
*/10 * * * * /usr/local/bin/monitoring.sh
```

### Verificación del Servicio
```bash
sudo crontab -l
sudo systemctl status cron
```

---

## 13. LibreSpeed

### ¿Qué es LibreSpeed?
**LibreSpeed** es una herramienta de test de velocidad de red de código abierto, altamente ligera, escrita en JavaScript e impulsada por un backend modular. Permite medir con precisión parámetros clave de conectividad:
* Velocidad de descarga (*Download*).
* Velocidad de subida (*Upload*).
* Latencia de red (*Ping*).
* Variación de retardo (*Jitter*).
* Dirección IP pública del cliente, ISP y telemetría opcional.

* **Repositorio oficial:** [https://github.com/librespeed/speedtest](https://github.com/librespeed/speedtest)

---

## 14. Lighttpd

Para servir la aplicación web de LibreSpeed sin sobrecargar el servidor con entornos pesados, se emplea **Lighttpd**, un servidor HTTP optimizado para consumir un mínimo de recursos de CPU y memoria.

### Instalación y Activación
```bash
sudo apt update
sudo apt install lighttpd
sudo systemctl enable lighttpd
sudo systemctl start lighttpd
```

### Verificación del Servicio y Puerto
```bash
sudo systemctl status lighttpd
sudo ss -ltnp | grep ':80'
```

### Configuración de la Raíz Web
El directorio raíz por defecto debe apuntar a `/var/www/html`:
```bash
grep -n "server.document-root" /etc/lighttpd/lighttpd.conf
```
Asegurando los siguientes valores en la configuración:
```text
server.document-root = "/var/www/html"
server.port = 80
```

---

## 15. PHP

Dado que LibreSpeed requiere un motor de procesamiento backend, se instala PHP junto con los módulos CGI necesarios para integrarse perfectamente con Lighttpd.

### Instalación de Paquetes PHP
```bash
sudo apt install php-cgi php-cli php-curl php-mysql php-sqlite3
```

### Verificación de la Versión
```bash
php -v
```

### Activación de Módulos FastCGI en Lighttpd
```bash
sudo lighttpd-enable-mod fastcgi
sudo lighttpd-enable-mod fastcgi-php
```

### Validación y Reinicio del Servidor Web
```bash
sudo lighttpd -t -f /etc/lighttpd/lighttpd.conf
sudo systemctl restart lighttpd
```

---

## 16. Instalación de LibreSpeed

Se descarga y despliega el repositorio oficial directamente en el directorio raíz del servidor web:

```bash
cd /var/www/html
sudo git clone https://github.com/librespeed/speedtest.git librespeed
```

### Estructura de Archivos Resultante
```text
/var/www/html/
└── librespeed/
    ├── backend/
    ├── frontend/
    ├── index.html
    ├── index-classic.html
    ├── index-modern.html
    ├── speedtest.js
    ├── speedtest_worker.js
    ├── config.json
    └── settings.json
```

### Ajuste de Permisos y Propietarios
Para garantizar que el servidor web pueda leer y servir los archivos de manera segura:
```bash
sudo chown -R www-data:www-data /var/www/html/librespeed
sudo chmod -R 755 /var/www/html/librespeed
```

### Acceso a la Aplicación
* **Acceso directo en la VM:** `http://IP_DE_LA_VM/librespeed/`
* **Acceso mediante reenvío de puertos (Host):** `http://localhost:8080/librespeed/`

---

## 17. Configuración de VirtualBox

Para interactuar con la máquina virtual desde el sistema operativo anfitrión (*host*), se configuran reglas de reenvío de puertos (*Port Forwarding*) en las opciones de red NAT de VirtualBox.

### Configuración de Red para SSH
| Parámetro de Red | Valor Configurado |
| :--- | :--- |
| **Protocolo** | TCP |
| **IP del Host** | `127.0.0.1` |
| **Puerto del Host** | `4241` |
| **IP de la Guest (VM)** | *(IP interna asignada)* |
| **Puerto de la Guest** | `4241` |

*Comando de acceso resultante:*
```bash
ssh dcasasol42@localhost -p 4241
```

### Configuración de Red para LibreSpeed (HTTP)
| Parámetro de Red | Valor Configurado |
| :--- | :--- |
| **Protocolo** | TCP |
| **IP del Host** | `127.0.0.1` |
| **Puerto del Host** | `8080` |
| **IP de la Guest (VM)** | *(IP interna asignada)* |
| **Puerto de la Guest** | `80` |

### Esquema de Red (NAT Port Forwarding)
```text
Host (localhost:8080) ──► VirtualBox NAT ──► Debian VM (Puerto 80 / Lighttpd) ──► LibreSpeed
```
> 💡 *Nota:* Para evaluaciones o pruebas de rendimiento de red más realistas, se puede alternar el adaptador de red a modo **Adaptador Puente (*Bridged Adapter*)**, permitiendo que la máquina virtual obtenga una dirección IP propia directamente dentro de la red local física.

---

## 18. Comprobaciones

Conjunto de comandos rápidos recomendados para verificar el estado integral de la infraestructura del servidor:

### Sistema y Recursos
```bash
hostnamectl
uname -a
free -h
df -h
```

### Almacenamiento LVM
```bash
lsblk
sudo pvs
sudo vgs
sudo lvs
```

### Usuarios y Permisos
```bash
groups dcasasol42
getent group sudo
getent group user42
```

### Red y Seguridad (SSH, UFW, AppArmor)
```bash
sudo sshd -t
sudo systemctl status ssh
sudo ss -ltnp | grep 4241
sudo ufw status verbose
sudo aa-status
```

### Monitorización y Automatización
```bash
sudo bash /usr/local/bin/monitoring.sh
sudo crontab -l
sudo systemctl status cron
```

### Servicios Web (Lighttpd + PHP + LibreSpeed)
```bash
sudo systemctl status lighttpd
sudo ss -ltnp | grep ':80'
php -v
curl http://localhost/librespeed/
```

---

## 19. Problemas encontrados y soluciones

### 1. Conflicto de puertos con Nginx al desplegar servicios web
* **Síntoma:** Al intentar arrancar el servidor web Nginx, se devolvió el error crítico:
  ```text
  bind() to 0.0.0.0:80 failed (98: Address already in use)
  ```
* **Diagnóstico:** El puerto `80` ya se encontraba ocupado y en escucha activa por otro daemon del sistema operativo:
  ```bash
  sudo ss -ltnp | grep ':80'
  ```
  *Resultado:* Se identificó que `lighttpd` estaba acaparando el puerto.
* **Solución:** Se decidió unificar el stack tecnológico empleando **Lighttpd** de forma nativa para alojar LibreSpeed, evitando la duplicidad de servidores web innecesarios en un entorno minimalista.

### 2. El comando `wall` no transmitía las notificaciones a las terminales
* **Síntoma:** Al ejecutar el script de monitorización, el comando `wall` no enviaba texto a los usuarios conectados y el comando `who` no listaba sesiones activas debido a la ausencia del archivo de seguimiento de sesiones (`/run/utmp`).
* **Diagnóstico:** Los daemons de gestión de sesiones de systemd se encontraban detenidos:
  ```text
  dbus.socket      → inactive
  dbus.service     → inactive
  systemd-logind   → inactive
  ```
* **Solución:** Se activaron e iniciaron los servicios de control de sistema necesarios mediante systemctl:
  ```bash
  sudo systemctl start dbus.socket
  sudo systemctl start dbus
  sudo systemctl start systemd-logind
  ```
  Esto permitió que `pam_systemd` registrara adecuadamente las sesiones SSH concurrentes y habilitara el funcionamiento correcto de `wall`.

---

## 20. Comandos útiles para la defensa

* **¿Cómo comprobar el hostname actual?**
  ```bash
  hostnamectl
  ```
* **¿Cómo verificar los grupos a los que pertenece un usuario?**
  ```bash
  groups dcasasol42
  ```
* **¿Cómo comprobar la arquitectura y volúmenes de LVM?**
  ```bash
  lsblk && sudo pvs && sudo vgs && sudo lvs
  ```
* **¿Qué es LVM y qué ventajas aporta?**
  LVM (*Logical Volume Manager*) es un gestor de volúmenes lógicos que introduce una capa de abstracción entre el soporte físico de almacenamiento y los sistemas de archivos. Su estructura conceptual es:
  $$\text{Physical Volume (PV)} \rightarrow \text{Volume Group (VG)} \rightarrow \text{Logical Volume (LV)} \rightarrow \text{Filesystem}$$
  Permite redimensionar particiones en caliente de manera flexible sin apagar el equipo.
* **¿Qué es UFW?**
  Es una interfaz simplificada para gestionar las reglas de filtrado de paquetes de Netfilter en Linux. Se verifica mediante:
  ```bash
  sudo ufw status verbose
  ```
* **¿Por qué se modifica el puerto por defecto de SSH?**
  Cambiar el puerto estándar (22) por un puerto no estándar (como `4241` o `4242`) reduce drásticamente el ruido generado por bots automatizados de fuerza bruta e intentos de intrusión masivos en la red. Sin embargo, no constituye una medida de seguridad aislada, sino que debe complementarse con la desactivación de accesos directos de root, llaves criptográficas o contraseñas robustas.
* **¿Qué es AppArmor?**
  Es un sistema de Control de Acceso Obligatorio (MAC) basado en perfiles que restringe las acciones que los procesos en ejecución y programas pueden realizar sobre el sistema de archivos del sistema operativo.
* **¿Cómo funciona el script de monitorización (`monitoring.sh`)?**
  Recopila métricas del kernel y hardware (CPU, memoria RAM, espacio en disco, carga del sistema, conexiones TCP, usuarios activos, direcciones IP/MAC y registros de comandos sudo) y los difunde masivamente a todas las terminales mediante `wall`.
* **¿Para qué sirve cron?**
  Es el planificador de procesos en segundo plano de Unix que ejecuta tareas recurrentes de forma automatizada según una expresión horaria definida (en este proyecto, cada 10 minutos mediante `*/10 * * * *`).
* **¿Qué es Lighttpd?**
  Un servidor web HTTP de alto rendimiento diseñado específicamente para entornos con restricciones de recursos, optimizado para consumir poca memoria RAM y CPU.

---

## 21. Checklist

Verificación final previa a la evaluación oficial:

- [ ] Máquina virtual creada y configurada correctamente en VirtualBox.
- [ ] Debian instalado en modo texto sin entorno gráfico.
- [ ] Hostname configurado acorde a las normas del proyecto (`<login>42`).
- [ ] Usuario principal añadido al grupo `sudo`.
- [ ] Usuario principal añadido al grupo `user42`.
- [ ] Estructura de almacenamiento mediante **LVM** correctamente implementada y montada.
- [ ] Política estricta de contraseñas configurada con `libpam-pwquality`.
- [ ] Políticas de caducidad de claves configuradas en `/etc/login.defs`.
- [ ] Configuración avanzada y segura de `sudo` aplicada.
- [ ] Servidor OpenSSH instalado y en funcionamiento.
- [ ] Acceso directo de `PermitRootLogin no` aplicado en SSH.
- [ ] Puerto SSH modificado y verificado.
- [ ] Firewall UFW activo con los puertos mínimos indispensables abiertos.
- [ ] Módulo AppArmor activo y operativo en el sistema.
- [ ] Script de monitorización (`monitoring.sh`) creado y ubicado en su ruta.
- [ ] Tarea programada en `cron` ejecutándose cada 10 minutos.
- [ ] Comando `wall` difundiendo correctamente las métricas a las terminales activas.
- [ ] Servidor web Lighttpd activo y sirviendo peticiones.
- [ ] Módulos FastCGI y PHP configurados y operativos.
- [ ] LibreSpeed desplegado y accesible correctamente desde el navegador.
- [ ] Reenvío de puertos (*Port Forwarding*) de VirtualBox comprobado.
- [ ] **Snapshot de seguridad** de la máquina virtual realizado antes de la defensa.

---

## 📚 Fuentes

* [Documentación Oficial de Debian](https://www.debian.org/doc/)
* [Guía de Referencia Born2beRoot (GitBook / Red 42)](https://www.gitbook.com/)
* [Repositorio Oficial de LibreSpeed — GitHub](https://github.com/librespeed/speedtest)
* [Documentación oficial de Lighttpd y PHP](https://www.lighttpd.net/)

---

## 🏁 Conclusión

Este proyecto consolida los fundamentos clave de la administración de sistemas Unix y Linux bajo un enfoque de endurecimiento de seguridad (*hardening*):

$$\text{Virtualización} \longrightarrow \text{Debian Minimal} \longrightarrow \text{LVM} \longrightarrow \text{Control de Accesos} \longrightarrow \text{Red y Firewall} \longrightarrow \text{Automatización} \longrightarrow \text{Servicios Web}$$

La máquina virtual resultante opera como un servidor robusto, optimizado y auditado desde la línea de comandos, preparado para resistir auditorías exigentes y garantizar un rendimiento óptimo en producción.