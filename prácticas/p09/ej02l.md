# Ejercicio 2l

## Primer intento

```
G12 = ⟨{S,A}, {a,d}, P12, S⟩

P12:
S → Aa | a
A → Sd | d
```

**Anulables**

No hay producciones anulables.

**Primeros**

```
Prim(S) = Prim(Aa) ∪ Prim(a) = {a, d}
Prim(A) = Prim(Sd) ∪ Prim(d) = {a, d}
```

**Siguientes**

```
Sig(S) = Prim(d) ∪ {$} = {d, $}
Sig(A) = Prim(a) = {a}
```

**Símbolos directrices**

```
SD(S → Aa) = Prim(Aa) = {a}
SD(S → a) = Prim(a) = {a}
SD(A → Sd) = Prim(Sd) = {d}
SD(A → d) = Prim(d) = {d}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular:
- `SD(S → Aa) ∩ SD(S → a) = {a} ≠ Ø`
- `SD(A → Sd) ∩ SD(A → d) = {d} ≠ Ø`

## Segundo intento

La gramática genera un lenguaje con las siguientes características:

- Todas las cadenas terminan con `a`.
- Las cadenas pueden empezar con `a` o con `d`.
- Las cadenas alternan entre `a` y `d`. Es decir, nunca hay 2 `a` o 2 `d` seguidas.

Ejemplos de cadenas que están en el lenguaje:

- `a`
- `da`
- `ada`
- `dada`
- `adada`

El conflicto proviene de que las producciones tienen recursión a izquierda indirecta, por ejemplo: `S ⇒ Aa ⇒ Sda`. Otra forma de verlo es que las producciones generan la cadena de derecha a izquierda. Pero el parser LL(1) usa una estrategia "leftmost derivation", derivación a izquierda (la segunda L en LL(1) indica ese detalle). Por la estructura de las cadenas del lenguaje, cuando por ejemplo consumimos una `a` no vamos a poder saber con un único lookahead si tenemos que usar la producción `S → Aa` o `S → a`. Depende si después de la `a` viene una `d` o si termina la cadena.

**Eliminación de la recursión a izquierda indirecta de `S`**

```
G12 = ⟨{S,A}, {a,d}, P12, S⟩

P12:
S → Sda | da | a
A → Sd | d
```

**Eliminación de no terminal inalcanzable `A`**

Después de haber eliminado la recursión a izquierda indirecta de `S` vemos que el no terminal `A` es inalcanzable desde el start symbol `S`, por lo tanto podemos eliminarlo junto a sus producciones de la gramática.

```
G12 = ⟨{S}, {a,d}, P12, S⟩

P12:
S → Sda | da | a
```

**Eliminación de la recursión a izquierda directa de `S`**

```
G12 = ⟨{S,T}, {a,d}, P12, S⟩

P12:
S → daT | aT
T → daT | λ
```

**Anulables**

```
T ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(daT) ∪ Prim(aT) = {a, d}
Prim(T) = Prim(daT) = {d}
```

**Siguientes**

```
Sig(S) = {$}
Sig(T) = Sig(S) ∪ Sig(T) = {$}
```

**Símbolos directrices**

```
SD(S → daT) = Prim(daT) = {d}
SD(S → aT) = Prim(aT) = {a}
SD(T → daT) = Prim(daT) = {d}
SD(T → λ) = Sig(T) = {$}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`d`|`$`|
|-|-|-|-|
|`S`|`S → aT`|`S → daT`||
|`T`||`T → daT`|`T → λ`|

</div>
