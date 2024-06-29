# Ejercicio 2g

```
G7 = ⟨{A}, {0,1}, P7, A⟩

P7:
A → 0A1 | 01
```

El lenguaje generado por esta gramática son las cadenas: $\{ 0^n1^n ∣ n ≥ 1 \}$.

A simple vista esta gramática va a tener un problema parecido al inciso f). Cuando consumimos un `0` no vamos a saber qué producción usar ya que la gramática es ambigua. Puntualmente no podemos saber si es el último `0` o no.

Podemos desambiguar la gramática forzando el primer `01` en la producción de `A` y luego agregar un nuevo no terminal `B` para generar el resto de los `01`s (puede no haber ninguno más).

**Gramática desambiguada**

```
G7 = ⟨{A,B}, {0,1}, P7, A⟩

P7:
A → 0B1
B → 0B1 | λ
```

**Anulables**

```
B ⇒* λ
```

**Primeros**

```
Prim(A) = Prim(0B1) = {0}
Prim(B) = Prim(0B1) = {0}
```

**Siguientes**

```
Sig(A) = {$}
Sig(B) = Prim(1) = {1}
```

**Símbolos directrices**

```
SD(A → 0B1) = Prim(0B1) = {0}
SD(B → 0B1) = Prim(0B1) = {0}
SD(B → λ) = Sig(B) = {1}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`0`|`1`|`$`|
|-|-|-|-|
|`A`|`A → 0B1`||
|`B`|`B → 0B1`|`B → λ`|

</div>

**Seguimiento**

| Pila | Entrada | Producción |
|-|-|-|
|`A$`|`000111$`|`A → 0B1`|
|~~`0`~~ `B1$`|~~`0`~~ `00111$`|`B → 0B1`|
|~~`0`~~ `B11$`|~~`0`~~ `0111$`|`B → 0B1`|
|~~`0`~~ `B111$`|~~`0`~~ `111$`|`B → λ`|
|~~`111$`~~|~~`111$`~~|**Aceptar**|
