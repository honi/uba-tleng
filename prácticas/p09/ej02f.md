# Ejercicio 2f

## Primer intento

```
G6 = ⟨{S}, {a}, P6, S⟩

P6:
S → aS | a
```

**Anulables**

No hay producciones anulables.

**Primeros**

```
Prim(S) = Prim(aS) ∪ Prim(a) = {a}
```

**Siguientes**

```
Sig(S) = {$}
```

**Símbolos directrices**

```
SD(S → aS) = Prim(aS) = {a}
SD(S → a) = Prim(a) = {a}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular `SD(S → aS) ∩ SD(S → a) = {a} ≠ Ø`.

## Segundo intento

El lenguaje generado es `a+`. El conflicto es que al consumir una `a` no sabemos si es la última o no. Cambiemos la gramática para que sea más parecido a reconocer `aa*`, es decir, forzamos consumir la primer `a` y luego, con otra producción, consumir el resto de las `a`.

```
G6 = ⟨{S,T}, {a}, P6, S⟩

P6:
S → aT
T → aT | λ
```

**Anulables**

```
T ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(aT) = {a}
Prim(T) = Prim(aT) = {a}
```

**Siguientes**

```
Sig(S) = {$}
Sig(T) = Sig(S) = {$}
```

**Símbolos directrices**

```
SD(S → aT) = Prim(aT) = {a}
SD(T → aT) = Prim(a) = {a}
SD(T → λ) = Sig(T) = {$}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`$`|
|-|-|-|
|`S`|`S → aT`||
|`T`|`T → aT`|`T → λ`|

</div>
