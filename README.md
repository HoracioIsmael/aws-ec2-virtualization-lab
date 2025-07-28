# 🌐 Laboratorio de Virtualización y Redes con AWS EC2

Este proyecto documenta un laboratorio personal en el que se aprovisionó y configuró una instancia EC2 de Amazon Web Services (AWS) con el objetivo de instalar y ejecutar un entorno de simulación Android para el juego _Evony: The King's Return_, y al mismo tiempo aplicar conceptos fundamentales de redes en la nube.

## 🎯 Objetivo del Proyecto

- Ejecutar un simulador Android en la nube para testear bots y scripts vinculados al juego _Evony_.
- Aplicar en la práctica conceptos de virtualización, seguridad de red y aprovisionamiento en la nube usando servicios de AWS.
- Construir un entorno completo que simula una red real con control de puertos, conexión remota y direccionamiento IP.

## 🛠️ Tecnologías y Servicios Utilizados

- **Amazon EC2** – Elastic Compute Cloud
- **Amazon VPC** – Virtual Private Cloud
- **Security Groups** – Reglas de firewall definidas por el usuario
- **Elastic IP** – IP pública estática para acceso remoto
- **Ubuntu Server / Windows Server** como sistema operativo en la instancia
- **Android Emulator** o **Nox Player** en la VM
- **SSH** – Conexión remota a la instancia

## 🔧 Configuración y Pasos Realizados

### 1. Aprovisionamiento de la Instancia

- Se lanzó una instancia EC2 tipo `t2.medium` desde una Amazon Machine Image (AMI) de Windows Server 2019 y/o Ubuntu 20.04.
- Se asignó una Elastic IP para mantener la dirección pública fija.
- Se configuraron volúmenes persistentes (EBS) para los datos.

### 2. Configuración de Seguridad (Security Groups)

- Se abrió el puerto `3389` para conexión RDP en Windows, o el puerto `22` para conexión SSH si se utilizó Ubuntu.
- Se bloquearon accesos no deseados limitando las IPs permitidas desde donde se podía acceder.
- Se aplicó control de puertos para la aplicación en pruebas.

### 3. Instalación del Entorno

- Se accedió vía RDP o SSH y se procedió a la instalación de:
  - **Nox Player** como simulador Android.
  - Bots de automatización para _Evony_.
  - Scripts Python y herramientas de monitoreo de red.
  - Chrome, drivers de audio/vídeo, y herramientas de escritorio si era Linux.
  - OpenVPN o proxy local si se necesitaba enrutar tráfico.

### 4. Gestión de Red y Virtualización

- Se configuró una **Elastic IP** con el objetivo de mantener la conexión remota aún después de reinicios.
- Se realizó pruebas con IP dinámica vs IP fija.
- Se analizó el consumo de CPU, RAM y tráfico bajo condiciones de simulación de juego intensivo.
- Se realizaron redirecciones de puertos para pruebas de conexión desde dispositivos externos.

## 📘 Lecciones Aprendidas

- Cómo lanzar, configurar y asegurar una instancia EC2 desde cero.
- Cómo gestionar puertos y conexiones con **Security Groups** personalizados.
- Experiencia práctica en manejo de direcciones IP públicas, privadas y NAT.
- Uso de máquinas virtuales en la nube como plataforma para software de alta demanda gráfica.
- Diagnóstico y solución de errores frecuentes (conexión, latencia, cierre por inactividad).
- Validación de conceptos de redes reales como puenteo, forwarding y tunneling aplicados al juego.

## 📎 Consideraciones Finales

> Si bien el laboratorio se usó para un entorno de juego, su diseño, configuración y aplicación se vincula directamente con entornos reales que demandan alta disponibilidad, uso de scripts automatizados y comprensión sólida de redes en la nube.

Este proyecto demuestra no solo habilidades técnicas, sino también creatividad, autonomía de aprendizaje y capacidad de aplicar infraestructura cloud a contextos no tradicionales.

## 👤 Autor

**Horacio Ismael Correa**  
Docente Técnico, UTN Argentina  
Contacto: [LinkedIn](horacio-ismael-correa) | [Email](horacioismelcorrea@gmail.com)
