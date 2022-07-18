Grid Convergence Study (Linux)
==============================

Summary
-------

This is a grid convergence study of 5 cases. The case with the finest
grid resolution, of 0.0625m, achieved an asymptotic ratio of 1.003
(asymptotic range is indicated by a value :math:`\approx 1`). At zero
grid resolution, the normalised velocity deficit measured 1.2 diameters
downstream from the turbine was 43.04%, a 13.78% error against the
measured value of 49.92% for the 3% ambient turbulence intensity (TI)
experiment. At zero grid resolution the turbulence intensity measured
1.2 diameters downstream from the turbine was 10.01%, an error of 45.71%
against the measured value of 21.9% for the 3% ambient TI experiment.
The simulated ambient TI, at zero grid resolution, is 5.47%.

For the centreline velocity (3% TI) transect, the root mean square error
at the lowest grid resolution was 0.2004 (m/s). For the centreline
velocity (15% TI) transect, the root mean square error at the lowest
grid resolution was 0.09075 (m/s). For the axial velocity at
:math:`x^*=5` (3% TI) transect, the root mean square error at the lowest
grid resolution was 0.1232 (m/s). For the axial velocity at
:math:`x^*=5` (15% TI) transect, the root mean square error at the
lowest grid resolution was 0.05688 (m/s). For the centreline turbulence
intensity (3% TI) transect, the root mean square error at the lowest
grid resolution was 6.543 (%). For the centreline turbulence intensity
(15% TI) transect, the root mean square error at the lowest grid
resolution was 10.31 (%).

Grid Convergence Studies
------------------------

Free Stream Velocity
~~~~~~~~~~~~~~~~~~~~

This section presents the convergence study for the free stream velocity
(:math:`U_\infty`). For the final case, with grid resolution of 0.0625m,
an asymptotic ratio of 1.63 was achieved (asymptotic range is indicated
by a value :math:`\approx 1`). The free stream velocity at zero grid
resolution is 0.8046m/s. The grid resolution required for a fine-grid
GCI of 1.0% is 0.03862m.

.. table:: Free stream velocity (:math:`U_\infty`) per grid resolution
           with computational cells and error against value at zero grid resolution

   ============== ======= ====================== ==========
   resolution (m) # cells :math:`U_\infty` (m/s) error
   ============== ======= ====================== ==========
   1              144     0.756681               0.0595774
   0.5            1152    0.790921               0.0170231
   0.25           9216    0.793301               0.0140647
   0.125          73728   0.794949               0.0120171
   0.0625         589824  0.797055               0.00939923
   ============== ======= ====================== ==========

.. figure:: u_infty_convergence.png
   :alt: Free stream velocity error against value at zero grid
         resolution per grid resolution
   :width: 3.64in

   Free stream velocity error against value at zero grid resolution per
   grid resolution

Free Stream Turbulence Intensity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section presents the convergence study for the free stream
turbulence intensity (:math:`I_\infty`). For the final case, with grid
resolution of 0.0625m, an asymptotic ratio of 2.029 was achieved
(asymptotic range is indicated by a value :math:`\approx 1`). The free
stream velocity at zero grid resolution is 5.47%. The grid resolution
required for a fine-grid GCI of 1.0% is 0.003269m.

.. table:: Free stream turbulence intensity (:math:`I_\infty`) per grid
           resolution with computational cells and error against value at zero grid
           resolution

   ============== ======= ==================== =========
   resolution (m) # cells :math:`I_\infty` (%) error
   ============== ======= ==================== =========
   1              144     4.60414              0.158243
   0.5            1152    3.47658              0.364391
   0.25           9216    5.24653              0.0407978
   0.125          73728   5.18668              0.0517407
   0.0625         589824  5.27265              0.0360232
   ============== ======= ==================== =========

.. figure:: ti_infty_convergence.png
   :alt: Free stream turbulence intensity error against value at zero
         grid resolution per grid resolution
   :width: 3.64in

   Free stream turbulence intensity error against value at zero grid
   resolution per grid resolution

Wake Velocity
~~~~~~~~~~~~~

This section presents the convergence study for the wake centerline
velocity measured 1.2 diameters downstream from the turbine
(:math:`U_{1.2D}`). For the final case, with grid resolution of 0.0625m,
an asymptotic ratio of 1.003 was achieved (asymptotic range is indicated
by a value :math:`\approx 1`). The free stream velocity at zero grid
resolution is 0.4583m/s. The grid resolution required for a fine-grid
GCI of 1.0% is 0.1524m.

.. table:: Wake centerline velocity 1.2 diameters downstream
           (:math:`U_{1.2D}`) per grid resolution with computational cells and
           error against value at zero grid resolution

   ============== ======= ====================== ==========
   resolution (m) # cells :math:`U_{1.2D}` (m/s) error
   ============== ======= ====================== ==========
   1              144     0.736009               0.605977
   0.5            1152    0.644324               0.405919
   0.25           9216    0.515944               0.125793
   0.125          73728   0.45951                0.00265518
   0.0625         589824  0.458319               5.6044e-05
   ============== ======= ====================== ==========

.. figure:: u_wake_convergence.png
   :alt: Wake velocity error against value at zero grid resolution per
         grid resolution
   :width: 3.64in

   Wake velocity error against value at zero grid resolution per grid
   resolution

Wake Turbulence Intensity
~~~~~~~~~~~~~~~~~~~~~~~~~

This section presents the convergence study for the wake centerline
turbulence intensity (TI) measured 1.2 diameters downstream from the
turbine (:math:`I_{1.2D}`). For the final case, with grid resolution of
0.0625m, an asymptotic ratio of 1.036 was achieved (asymptotic range is
indicated by a value :math:`\approx 1`). TI at zero grid resolution is
10.01%. The grid resolution required for a fine- grid GCI of 1.0% is
0.05952m.

.. table:: Wake centerline TI 1.2 diameters downstream
           (:math:`I_{1.2D}`) per grid resolution with computational cells and
           error against value at zero grid resolution

   ============== ======= ===================== ==========
   resolution (m) # cells :math:`I_{1.2D} (\%)` error
   ============== ======= ===================== ==========
   1              144     4.63007               0.537339
   0.5            1152    4.96932               0.50344
   0.25           9216    12.3321               0.23229
   0.125          73728   10.4663               0.0458488
   0.0625         589824  10.0981               0.00904952
   ============== ======= ===================== ==========

.. figure:: ti_wake_convergence.png
   :alt: Wake TI error against value at zero grid resolution per grid
         resolution
   :width: 3.64in

   Wake TI error against value at zero grid resolution per grid
   resolution

Validation
~~~~~~~~~~

At zero grid resolution, the normalised deficit of :math:`U_{1.2D}`,
(:math:`\gamma_{0(1.2D)}`) is 43.04%, a 13.78% error against the
measured value of 49.92%.

Wake Transects
--------------

This section presents axial velocity transects along the turbine
centreline and at cross-sections along the :math:`y`-axis. Errors are
reported relative to the experimental data given in (Mycek et al. 2014).

Centreline velocity (3% TI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root mean square error (RMSE) for this transect at the finest grid
resolution of 0.0625m was 0.2004 (m/s).

.. table:: Root mean square error (RMSE) for the normalised velocity,
           :math:`u^*_0`, per grid resolution.

   ============== ==========
   resolution (m) RMSE (m/s)
   ============== ==========
   1              0.401335
   0.5            0.271788
   0.25           0.239064
   0.125          0.190003
   0.0625         0.200371
   ============== ==========

.. figure:: transect_u0_0.png
   :alt: Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
         comparison. Experimental data reverse engineered from (Mycek et al.
         2014, fig. 11a).
   :width: 5.68in

   Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
   comparison. Experimental data reverse engineered from (Mycek et al.
   2014, fig. 11a).

.. figure:: transect_gamma0_0.png
   :alt: Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
         resolution comparison. Experimental data reverse engineered from
         (Mycek et al. 2014, fig. 11a).
   :width: 5.68in

   Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
   resolution comparison. Experimental data reverse engineered from
   (Mycek et al. 2014, fig. 11a).

Centreline velocity (15% TI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root mean square error (RMSE) for this transect at the finest grid
resolution of 0.0625m was 0.09075 (m/s).

.. table:: Root mean square error (RMSE) for the normalised velocity,
           :math:`u^*_0`, per grid resolution.

   ============== ==========
   resolution (m) RMSE (m/s)
   ============== ==========
   1              0.203884
   0.5            0.136543
   0.25           0.0818053
   0.125          0.101083
   0.0625         0.0907545
   ============== ==========

.. figure:: transect_u0_1.png
   :alt: Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
         comparison. Experimental data reverse engineered from (Mycek et al.
         2014, fig. 11b).
   :width: 5.68in

   Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
   comparison. Experimental data reverse engineered from (Mycek et al.
   2014, fig. 11b).

.. figure:: transect_gamma0_1.png
   :alt: Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
         resolution comparison. Experimental data reverse engineered from
         (Mycek et al. 2014, fig. 11b).
   :width: 5.68in

   Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
   resolution comparison. Experimental data reverse engineered from
   (Mycek et al. 2014, fig. 11b).

Axial velocity at :math:`x^*=5` (3% TI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root mean square error (RMSE) for this transect at the finest grid
resolution of 0.0625m was 0.1232 (m/s).

.. table:: Root mean square error (RMSE) for the normalised velocity,
           :math:`u^*_0`, per grid resolution.

   ============== ==========
   resolution (m) RMSE (m/s)
   ============== ==========
   1              0.201806
   0.5            0.134912
   0.25           0.135605
   0.125          0.118328
   0.0625         0.123211
   ============== ==========

.. figure:: transect_u0_2.png
   :alt: Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
         comparison. Experimental data reverse engineered from (Mycek et al.
         2014, fig. A12a).
   :width: 5.68in

   Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
   comparison. Experimental data reverse engineered from (Mycek et al.
   2014, fig. A12a).

.. figure:: transect_gamma0_2.png
   :alt: Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
         resolution comparison. Experimental data reverse engineered from
         (Mycek et al. 2014, fig. A12a).
   :width: 5.68in

   Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
   resolution comparison. Experimental data reverse engineered from
   (Mycek et al. 2014, fig. A12a).

Axial velocity at :math:`x^*=5` (15% TI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root mean square error (RMSE) for this transect at the finest grid
resolution of 0.0625m was 0.05688 (m/s).

.. table:: Root mean square error (RMSE) for the normalised velocity,
           :math:`u^*_0`, per grid resolution.

   ============== ==========
   resolution (m) RMSE (m/s)
   ============== ==========
   1              0.0474432
   0.5            0.0520709
   0.25           0.0470543
   0.125          0.0609816
   0.0625         0.056879
   ============== ==========

.. figure:: transect_u0_3.png
   :alt: Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
         comparison. Experimental data reverse engineered from (Mycek et al.
         2014, fig. A12a).
   :width: 5.68in

   Normalised velocity, :math:`u^*_0`, (m/s) per grid resolution
   comparison. Experimental data reverse engineered from (Mycek et al.
   2014, fig. A12a).

.. figure:: transect_gamma0_3.png
   :alt: Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
         resolution comparison. Experimental data reverse engineered from
         (Mycek et al. 2014, fig. A12a).
   :width: 5.68in

   Normalised velocity deficit, :math:`\gamma_0`, (%) per grid
   resolution comparison. Experimental data reverse engineered from
   (Mycek et al. 2014, fig. A12a).

Centreline turbulence intensity (3% TI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root mean square error (RMSE) for this transect at the finest grid
resolution of 0.0625m was 6.543 (%).

.. table:: Root mean square error (RMSE) for the turbulence intensity,
           :math:`I_0`, per grid resolution.

   ============== ========
   resolution (m) RMSE (%)
   ============== ========
   1              12.0893
   0.5            11.121
   0.25           6.18045
   0.125          6.62332
   0.0625         6.54326
   ============== ========

.. figure:: transect_I0_0.png
   :alt: Turbulence intensity, :math:`I_0`, (%) per grid resolution
         comparison. Experimental data reverse engineered from (Mycek et al.
         2014, fig. 11c).
   :width: 5.68in

   Turbulence intensity, :math:`I_0`, (%) per grid resolution
   comparison. Experimental data reverse engineered from (Mycek et al.
   2014, fig. 11c).

Centreline turbulence intensity (15% TI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root mean square error (RMSE) for this transect at the finest grid
resolution of 0.0625m was 10.31 (%).

.. table:: Root mean square error (RMSE) for the turbulence intensity,
           :math:`I_0`, per grid resolution.

   ============== ========
   resolution (m) RMSE (%)
   ============== ========
   1              15.5431
   0.5            14.7203
   0.25           9.71568
   0.125          10.3019
   0.0625         10.3063
   ============== ========

.. figure:: transect_I0_1.png
   :alt: Turbulence intensity, :math:`I_0`, (%) per grid resolution
         comparison. Experimental data reverse engineered from (Mycek et al.
         2014, fig. 11d).
   :width: 5.68in

   Turbulence intensity, :math:`I_0`, (%) per grid resolution
   comparison. Experimental data reverse engineered from (Mycek et al.
   2014, fig. 11d).

References
----------

.. container:: references csl-bib-body hanging-indent
   :name: refs

   .. container:: csl-entry
      :name: ref-mycek2014

      Mycek, Paul, Benoît Gaurier, Grégory Germain, Grégory Pinon, and
      Elie Rivoalen. 2014. “Experimental Study of the Turbulence
      Intensity Effects on Marine Current Turbines Behaviour. Part I:
      One Single Turbine.” *Renewable Energy* 66: 729–46.
      https://doi.org/10.1016/j.renene.2013.12.036.
