# Ejercicio 2e

*Renombramos `{` y `}` por `[` y `]` respectivamente.*

## Primer intento

```
G5 = ⟨{A}, {[,]}, P5, A⟩

P5:
A → A[A]A | λ
```

**Anulables**

```
A ⇒* λ
```

**Primeros**

```
Prim(A) = {[}
```

**Siguientes**

```
Sig(A) = {[, ], $}
```

**Símbolos directrices**

```
SD(A → A[A]A) = Prim(A[A]A) = {[}
SD(A → λ) = {[, ], $}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular `SD(A → A[A]A) ∩ SD(A → λ) = {[} ≠ Ø`.

## Segundo intento

Probamos eliminar la recursión a izquierda.

```
G5 = ⟨{A,B}, {[,]}, P5, A⟩

P5:
A → B
B → [A]AB | λ
```

**Anulables**

```
A ⇒* λ
B ⇒* λ
```

**Primeros**

```
Prim(A) = {[}
Prim(B) = {[}
```

**Siguientes**

```
Sig(A) = Prim(]) ∪ Prim(B) ∪ Sig(B) ∪ {$} = {[, ], $}
Sig(B) = Sig(A) = {[, ], $}
```

**Símbolos directrices**

```
SD(A → B) = Prim(B) ∪ Sig(A) = {[, ], $}
SD(B → [A]AB) = Prim([A]AB) = {[}
SD(B → λ) = Sig(B) = {[, ], $}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular `SD(B → [A]AB) ∩ SD(B → λ) = {[} ≠ Ø`.

## Tercer intento

Observemos que la gramática genera corchetes balanceados. Pero la producción no es leftmost ("a izquierda").

Llamemos un nivel de corchetes a todos los corchetes hijos del mismo corchete padre (los corchetes de nivel 0 no tienen padre). En un mismo nivel de corchetes la gramática permite generarlos en cualquier orden arbitrario: desde el centro de la cadena hacia la izquierda y/o derecha, de izquierda a derecha, de derecha a izquierda, etc.

Podemos reescribir la gramática y forzar una derivación siempre a izquierda. Se mantiene el mismo lenguaje pero sin ambigüedad.

```
G5 = ⟨{A}, {[,]}, P5, A⟩

P5:
A → [A]A | λ
```

**Anulables**

```
A ⇒* λ
```

**Primeros**

```
Prim(A) = {[}
```

**Siguientes**

```
Sig(A) = {], $}
```

**Símbolos directrices**

```
SD(A → [A]A) = Prim([A]A) = {[}
SD(A → λ) = Sig(A) = {], $}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`[`|`]`|`$`|
|-|-|-|-|
|A|`A → [A]A`|`A → λ`|`A → λ`|

</div>
