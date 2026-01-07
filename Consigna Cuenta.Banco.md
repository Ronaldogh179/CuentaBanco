## 📌 Consigna: Implementación de la clase `CuentaBanco` en Python (POO)

### 🎯 Objetivo

Desarrollar una aplicación en **Python utilizando Programación Orientada a Objetos (POO)** que modele el comportamiento básico de una **cuenta bancaria**, aplicando buenas prácticas de desarrollo de software, control de versiones con Git y el estándar de codificación **PEP-8**.

---

### 🧩 Descripción de la actividad

El docente proporcionará un repositorio base en GitHub llamado **`CuentaBanco`**.
Cada estudiante deberá **realizar un fork del repositorio** y completar la implementación solicitada siguiendo estrictamente las indicaciones de esta consigna.

---

### 🏗️ Requisitos de implementación

#### 1. Clase `CuentaBanco`

Implementar la clase `CuentaBanco` en Python, considerando encapsulamiento y validación de datos.

La clase debe incluir los siguientes métodos:

* **`deposito_cuenta(monto)`**

  * Permite depositar un monto a la cuenta.
  * El monto debe ser un valor numérico positivo.

* **`retiro_cuenta(monto)`**

  * Permite retirar un monto de la cuenta.
  * El monto debe ser positivo y no debe superar el saldo disponible.

* **`transferencia_cuenta(monto, cuenta_destino)`**

  * Permite transferir un monto desde una cuenta origen hacia otra cuenta bancaria.
  * Se debe validar el monto y la cuenta destino.

* **`saldo_cuenta()`**

  * Retorna o muestra el saldo actual de la cuenta.

📌 **Validaciones obligatorias**

* Validar tipos de datos y valores inválidos.
* No permitir montos negativos o cero.
* Manejar errores mediante excepciones (`ValueError`, `TypeError`, u otras según corresponda).

---

#### 2. Aplicación `app.py`

* Implementar un archivo `app.py` que permita interactuar con la clase `CuentaBanco` mediante un **menú desde la línea de comandos**.
* El menú debe permitir ejecutar todas las operaciones disponibles:

  1. Depósito
  2. Retiro
  3. Transferencia
  4. Consulta de saldo
  5. Salir

---

### 📁 Repositorio base (proporcionado por el docente)

El repositorio inicial contiene:

* La clase `CuentaBanco` **con el constructor ya implementado**.
* El archivo `app.py` que **únicamente crea el objeto**, sin lógica adicional.

⚠️ **No se debe modificar la estructura inicial del proyecto**, salvo para completar la funcionalidad solicitada.

---

### 🌿 Control de versiones (Git/GitHub)

* Cada funcionalidad debe desarrollarse en una **rama independiente**:

  * `feature/deposito`
  * `feature/retiro`
  * `feature/transferencia`
  * `feature/saldo`
* Una vez finalizada cada funcionalidad, debe **fusionarse con la rama `main`**.
* El historial de commits debe ser claro y descriptivo.

---

### 📐 Buenas prácticas

* El código debe cumplir estrictamente con el estándar **PEP-8**.
* Usar nombres de variables y métodos claros y representativos.
* Mantener métodos cortos, cohesionados y bien estructurados.

---

### ✅ Entregable

* Enlace al repositorio GitHub del estudiante (fork del repositorio `CuentaBanco`).
* El repositorio debe ejecutarse correctamente desde la línea de comandos.

---

### 📌 Criterios de evaluación (referencial)

* Correcta implementación de POO
* Validación y manejo de errores
* Funcionamiento del menú en `app.py`
* Uso adecuado de Git y ramas
* Cumplimiento del estándar PEP-8

## 📊 Rúbrica de evaluación – Proyecto *CuentaBanco* (Python POO)

| **Criterio / Indicador**                                                                                                           | **Sobresaliente (3)**                                                                                                                                                                                               | **Suficiente (2)**                                                                                                  | **En desarrollo (1)**                                                                                       | **Insatisfactorio (0)**                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Diseño POO de la clase CuentaBanco; uso correcto de encapsulamiento, atributos, constructor y cohesión de métodos.**             | La clase aplica correctamente POO, mantiene encapsulamiento, métodos cohesionados y responsabilidades claras; se evidencia diseño limpio y mejoras como uso de propiedades o separación clara de responsabilidades. | La clase cumple con POO básico, atributos y métodos están bien definidos; no presenta errores estructurales graves. | Uso parcial de POO; atributos o métodos mal definidos, acoplamiento excesivo o responsabilidades mezcladas. | No aplica POO; uso de variables globales, funciones sueltas o estructura incorrecta. |
| **Implementación del método depósito; validación de monto positivo, tipo de dato y actualización correcta del saldo.**             | Valida exhaustivamente el monto, maneja excepciones correctamente y actualiza el saldo sin errores; incluye mensajes o control adicional bien implementado.                                                         | Realiza el depósito correctamente y valida monto positivo; presenta validaciones básicas.                           | Permite depósitos incorrectos o carece de validación completa; errores menores en la lógica.                | No valida el monto o el método no funciona correctamente.                            |
| **Implementación del método retiro; validación de monto, control de saldo suficiente y manejo de errores.**                        | Valida monto y saldo, maneja excepciones adecuadas y evita estados inconsistentes; lógica clara y robusta.                                                                                                          | El retiro funciona y valida saldo suficiente; manejo básico de errores.                                             | Lógica incompleta; permite retiros inválidos o muestra errores de ejecución.                                | El método no funciona o permite saldo negativo sin control.                          |
| **Implementación del método transferencia; validación de monto, cuenta destino válida y actualización correcta de ambas cuentas.** | Transferencia completamente funcional, valida todos los parámetros y asegura consistencia entre cuentas; implementación clara y segura.                                                                             | La transferencia funciona y valida lo esencial; sin errores críticos.                                               | Transferencia parcial o con validaciones incompletas; errores menores de lógica.                            | No se implementa correctamente o genera errores graves.                              |
| **Consulta de saldo; retorno o visualización correcta del saldo actual de la cuenta.**                                             | Retorna el saldo de forma clara y consistente; uso adecuado del método y presentación correcta al usuario.                                                                                                          | Retorna o muestra el saldo correctamente sin errores.                                                               | El método existe pero presenta errores menores o salida confusa.                                            | El método no funciona o no está implementado.                                        |
| **Aplicación `app.py`; menú por consola completo, opciones funcionales y flujo correcto de interacción.**                          | Menú completo, intuitivo y robusto; todas las opciones funcionan correctamente y gestionan errores del usuario.                                                                                                     | Menú funcional con todas las opciones requeridas; interacción correcta.                                             | Menú incompleto o con errores de flujo; algunas opciones no funcionan correctamente.                        | No existe menú o la aplicación no ejecuta las funcionalidades.                       |
| **Validación y manejo de errores; uso adecuado de excepciones en todas las operaciones.**                                          | Manejo consistente de errores con excepciones bien tipadas y mensajes claros; sin fallos en ejecución.                                                                                                              | Manejo básico de errores; cubre los casos más comunes.                                                              | Manejo parcial de errores; excepciones no controladas en algunos casos.                                     | No se manejan errores; el programa falla ante entradas inválidas.                    |
| **Uso de Git y control de versiones; una rama por funcionalidad, fusiones correctas a main y commits claros.**                     | Uso ejemplar de Git; ramas bien nombradas, commits descriptivos y fusiones limpias sin conflictos.                                                                                                                  | Usa ramas por funcionalidad y realiza merges correctamente; commits aceptables.                                     | Uso irregular de ramas o merges incompletos; commits poco claros.                                           | Trabaja directamente en main o no usa control de versiones adecuadamente.            |
| **Estilo de código y cumplimiento de PEP-8; nombres claros, legibilidad y organización del código.**                               | Código completamente alineado a PEP-8; excelente legibilidad, nombres claros y estructura limpia.                                                                                                                   | Cumple mayormente PEP-8; errores menores de estilo.                                                                 | Presenta múltiples incumplimientos de PEP-8 que afectan la lectura.                                         | No respeta PEP-8; código desordenado y difícil de mantener.                          |
| **Funcionamiento general y calidad del entregable; ejecución sin errores y cumplimiento total de la consigna.**                    | El proyecto ejecuta correctamente, cumple todos los requisitos y aporta mejoras adicionales.                                                                                                                        | El proyecto ejecuta y cumple lo mínimo requerido.                                                                   | El proyecto ejecuta parcialmente o presenta fallos funcionales.                                             | El proyecto no ejecuta o no cumple la consigna.                                      |
