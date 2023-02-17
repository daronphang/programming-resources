## Z-index

Property sets the z-order of a positioned element (cannot be static) and its descendants or flex items. Overlapping elements with a larger z-index cover those with a smaller one.

### Stacking Context

A stacking context is formed by any element in the following scenarios:

- Root element of the document.
- Element that is positioned and z-index other than 'auto'.
- Element that is a child of a flex/grid container.

### Children (Nesting)

Children can never have z-index higher than their parent. Z-index vlaues of its child stacking contexts only have meaning in its parent.

### Siblings

Stacking contexts can be contained in other stacking contexts, and together create a hierarchy of stacking contexts. However, each stacking context is completely independent of its siblings i.e. elements within one stacking context do not participate along with elements within another stacking context.

Each stacking context is self-contained: after the element's contexts are stacked, the whole element is considered in the stacking order of the parent stacking context.
