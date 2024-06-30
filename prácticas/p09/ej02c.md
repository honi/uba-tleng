# Ejercicio 2c

## Primer intento

A priori no sabemos si esta gramática es LL(1). Podemos intentar armar la tabla de parsing y luego vemos si hay conflictos.

```
G3 = ⟨{S,A,B}, {a,b}, P3, S⟩

P3:
S → A | B
A → aA | λ
B → bB | λ
```

**Anulables**

```
S ⇒* λ
A ⇒* λ
B ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(A) ∪ Prim(B) = {a, b}
Prim(A) = Prim(aA) = {a}
Prim(B) = Prim(bB) = {b}
```

**Siguientes**

```
Sig(S) = {$}
Sig(A) = Sig(S) = {$}
Sig(B) = Sig(S) = {$}
```

**Símbolos directrices**

```
SD(S → A) = Prim(A) ∪ Sig(S) = {a, $}
SD(S → B) = Prim(B) ∪ Sig(S) = {b, $}
SD(A → aA) = Prim(aA) = {a}
SD(A → λ) = Sig(A) = {$}
SD(B → bB) = Prim(bB) = {b}
SD(B → λ) = Sig(B) = {$}
```

La gramática no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular `SD(S → A) ∩ SD(S → B) = {$} ≠ Ø`.

## Segundo intento

Los conflictos parecen provenir de que se puede producir `λ` desde cualquier no terminal. Modifiquemos la gramática para producir `λ` desde un único no terminal.

```
G3 = ⟨{S,A,B}, {a,b}, P3, S⟩

P3:
S → A | B | λ
A → aA | a
B → bB | b
```

El lenguaje es el mismo. Ahora solo obtenemos `λ` con la producción `S → λ`. Caso contrario, las cadenas que se pueden formar son `a+` o `b+` con las producciones desde `A` o `B` respectivamente.

**Anulables**

```
S ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(A) ∪ Prim(B) = {a, b}
Prim(A) = Prim(aA) ∪ Prim(a) = {a}
Prim(B) = Prim(bB) ∪ Prim(b) = {b}
```

**Siguientes**

```
Sig(S) = {$}
Sig(A) = Sig(S) = {$}
Sig(B) = Sig(S) = {$}
```

**Símbolos directrices**

```
SD(S → A) = Prim(A) = {a}
SD(S → B) = Prim(B) = {b}
SD(S → λ) = Sig(S) = {$}
SD(A → aA) = Prim(aA) = {a}
SD(A → a) = Prim(a) = {a}
SD(B → bB) = Prim(bB) = {b}
SD(B → b) = Prim(b) = {b}
```

La gramática aún no es LL(1) pues hay símbolos directrices que no son disjuntos, en particular `SD(A → aA) ∩ SD(A → a) = {a} ≠ Ø` y `SD(B → bB) ∩ SD(B → b) = {b} ≠ Ø`. Arreglamos un problema pero generamos otro, ahora hay conflictos en las producciones de `A` y `B`.

## Tercer intento

Mirando otra vez la gramática original, el conflicto estaba puntualmente en las producciones de `S`. Las producciones de `A` y `B` no tenían conflictos. Entonces quizás sería mejor transformar únicamente las producciones de `S`.

El conflicto es el siguiente: `SD(S → A) ∩ SD(S → B) = {$} ≠ Ø`. El símbolo `$` aparece en estos símbolos directrices porque al ser `A` y `B` anulables, se incluye `Sig(S)` en `SD(S → A)` y `SD(S → B)`. Busquemos evitar que eso pase.

```
G3 = ⟨{S,A,B}, {a,b}, P3, S⟩

P3:
S → aA | bB | λ
A → aA | λ
B → bB | λ
```

Ya sabemos que el lenguaje es `a*|b*`, o equivalentemente, `aa*|bb*|λ`. Al agregar la producción `S → λ` permitimos generar la cadena vacía directamente desde `S`. Ya que si usamos las otras producciones, forzamos empezar la cadena con una `a` o `b`. Y luego se pueden producir todas las `a` o `b` como uno quiera con las producciones de `A` o `B`.

**Anulables**

```
S ⇒* λ
A ⇒* λ
B ⇒* λ
```

**Primeros**

```
Prim(S) = Prim(aA) ∪ Prim(bB) = {a, b}
Prim(A) = Prim(aA) = {a}
Prim(B) = Prim(bB) = {b}
```

**Siguientes**

```
Sig(S) = {$}
Sig(A) = Sig(S) = {$}
Sig(B) = Sig(S) = {$}
```

**Símbolos directrices**

```
SD(S → aA) = Prim(aA) = {a}
SD(S → bB) = Prim(bB) = {b}
SD(S → λ) = Sig(S) = {$}
SD(A → aA) = Prim(aA) = {a}
SD(A → λ) = Sig(A) = {$}
SD(B → bB) = Prim(bB) = {b}
SD(B → λ) = Sig(B) = {$}
```

No hay conflictos!! 🥳

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`b`|`$`|
|-|-|-|-|
|S|`S → aA`|`S → bB`|`S → λ`|
|A|`A → aA`||`A → λ`|
|B||`B → bB`|`B → λ`|

</div>
