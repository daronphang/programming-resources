## Spline

```py
# spline function requires 1D + unique values

xsmooth = np.linspace(min(x_vals), max(x_vals), 200) 
spline = make_interp_spline(x_vals, y_vals, k=3)
ysmooth = spline(xsmooth)
ax.plot(xsmooth, ysmooth, marker=None, label=f'{fab.name}_kernel', color=fab.value)
``
