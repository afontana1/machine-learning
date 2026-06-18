# Worked Solutions

## Factor Product

Formula:

ψ(X,Y,Z) = φ₁(X,Y) · φ₂(Y,Z)

Example:

ψ(1,1,2) = 0.7 × 0.8 = 0.56

Interpretation:
Multiply compatible assignments from both factors.

---

## Factor Reduction

Given evidence:

Y = 1

Keep only rows where Y=1 and remove Y from the factor.

Interpretation:
Reduction is filtering.

---

## Factor Marginalization

Formula:

ψ(Y,Z) = Σₓ φ(X,Y,Z)

For each (Y,Z) pair, add all rows that differ only in X.

Example:

ψ(1,1) = 68 + 40 = 108

Interpretation:
Marginalization is group-by + sum.

---

## Independence

A and B are independent if:

P(A|B)=P(A)

and

P(B|A)=P(B)

These are equivalent definitions.
