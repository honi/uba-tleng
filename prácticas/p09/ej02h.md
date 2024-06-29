# Ejercicio 2h

```
G8 = ⟨{S}, {a,b}, P8, S⟩

P8:
S → aaSbb | a | λ
```

La gramática es ambigua porque al consumir una `a` no sabemos si es la `a` del medio de la cadena generada por la producción `S → a` o si es la primer `a` de la producción `S → aaSbb`.

Para desambiguar podemos modificar las producciones e introducir otro no terminal `T` que produce el resto de los símbolos que vienen luego de consumir una `a`: o bien `aSbb` o bien `λ` en el caso donde es la `a` del medio de la cadena.

```
G8 = ⟨{S,T}, {a,b}, P8, S⟩

P8:
S → aT | λ
T → aSbb | λ
```

**Anulables**

```
S ⇒* λ
T ⇒* λ
```

*Será un problema que ambos no terminales sean anulables...? Espero que no.*

**Primeros**

```
Prim(S) = {a}
Prim(T) = {a}
```

**Siguientes**

```
Sig(S) = {b, $}
Sig(T) = Sig(S) = {b, $}
```

**Símbolos directrices**

```
SD(S → aT) = Prim(aT) = {a}
SD(S → λ) = Sig(S) = {b, $}
SD(T → aSbb) = Prim(aSbb) = {a}
SD(T → λ) = Sig(T) = {b, $}
```

**Tabla de parsing LL(1)**

<div style="overflow-x:scroll; white-space: nowrap;">

||`a`|`b`|`$`|
|-|-|-|-|
|`S`|`S → aT`|`S → λ`|`S → λ`|
|`T`|`T → aSbb`|`T → λ`|`T → λ`|

</div>
