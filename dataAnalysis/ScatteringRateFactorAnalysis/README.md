# Scattering Rate Factor Analysis

Semiconductor devices are the basis of many devices from computers to LEDs to solar panels. The performance of these devices is based on how quickly and efficiently charge can move from one end of the device to the other. Defects in the device can cause carriers to scatter (i.e., lose energy). My Ph. D. dissertation is focused on how scattering from defects can cause the system to vibrate more and more violently, which can cause helpful atoms like hydrogen to be released from the defects thereby causing even more degradation of the device and its performance. 

Investigating this hydrogen release from first-principles quantum mechanics is a complex, multivariate problem. The electrons in the system can only occupy specific states (i.e., bands) and scattering causes the electrons to transition between the bands. The higher in energy the electron is, the more lower-energy states are available for it to potentially transition into. Higher-energy states can also transfer more energy to the system, which can accelerate degradation. However, higher-energy states are typically less likely. Every state not only has its own energy, but also its own spatial distribution of charge. In each state, the electron spreads out across the device in a different way, which causes the atoms to relax in different ways to accomodate. 

The calculations of the scattering rates are very expensive, so it would be helpful to determine ahead of time which states would likely have insignificant scattering rates. My goal in this project is to use a subset of the data to try to determine which variables most likely contribute to a significant transition rate. The core data I have are
* the energy of each state
* the electronic matrix elements between each of the states (i.e., how compatible the different electron states are with each other)
* the equilibrium positions each of the electronic states
* the resulting transition rate

The transition rate from one state to another (i.e., the probability of the transition) is dependent on the displacement between the equilibrium positions, the change in energy, and the electronic matrix elements between the involved states. More specifically, how the displacement maps onto the way that the atoms are already vibrating (i.e., the phonon modes of the system) determines how efficiently the energy could be distributed, which means the transition would be more likely. The vibrations of the system are broken into independent "coordinates" called phonon modes, which each have their own unique frequency of vibration and atomic displacements produced. All of the independent modes add together to provide the overall atomic movements. 

The displacement of the equilibrium atomic postitions between different states can be projected onto the phonon modes to show how closely the displacement matches up with each of the independent vibrations. The phonon modes are typically indexed with $j$ and the projection is called $\Delta q_{if}^{(j)}$, where the indices show that there is a different projection for each pair of states $i,f$ and each phonon mode $j$. There is also another factor called the Huang-Rhys factor $S_{if}^{(j)}$, which also depends on the pair of states and mode, that also includes the frequency $\omega_j$ for each phonon mode. The Huang-Rhys factor has long been used as a proxy for the significance of a mode for energy dissipation and, therefore, how likely the energy from a given transition is to be dissipated into each vibrational mode.

I would like to be able to understand and explain the results of this analysis, so I will need to simplify the present data. Instead of trying to predict a numerical value for the transition rate, I am going to split the transition rate $\Gamma_{if}$ into  low ($\Gamma_{if} < 10^6 \text{ s}^{-1}$), medium ($10^6 \text{ s}^{-1} < \Gamma_{if} < 10^9 \text{ s}^{-1}$), and high ($10^9 \text{ s}^{-1} < \Gamma_{if}$) significance categories. I will not consider the mode-related values explicitly, but I will instead aggregate across phonon modes using measures like max, mean, median Huang-Rhys factor for each transition, the remainder when the transition energy is divided by the mode energy ($\hbar \omega_j$) etc. 

