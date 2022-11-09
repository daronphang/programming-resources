## Flexbox vs Grid

Flexbox is designed for alignment (align-items, justify-content) while Grid is designed for layout.

Flexbox is designed for one dimension i.e. row or column. Grid is designed for two-dimensional layout i.e. rows and columns at the same time. Flexbox also works from the content out i.e. spacing items evenly in a container by letting size of the content decide how much individual space each item takes up.

In terms of wrapping, Flex will wrap down onto another row when the flex items fills a row, while Grid will fall along the same grid line as of all other elements. If you are using flexbox and disabling some of the flexibility i.e. setting % width on a flex item to make it line up with other items in the row above, gird is likely to be a better choice.

Flexbox requires negative margins, transform or absolute positioning in order to break out of flex behavior, while Grid can place items on overlapping grid lines or within the same grid cells.
