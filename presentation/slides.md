---
author: Maël Le Garrec
title: "LHC Effective Model for Optics Corrections"
subtitle: "PhD Thesis Presentation"
date: 2025-01-30
...

[//]: -----------------------
[//]:     Introduction
[//]: -----------------------


# Introduction

::: complete :::

\normalsize

* Introduction
    * Magnets and Optics
    * LHC-specific overview

\vspace{0.2cm}

* Thesis Work
    * Decapole Studies
    * Dodecapole Studies
    * Decatetrapole Studies

\vspace{0.5cm}

* Conclusion

:::

\includegraphics[width=0.8\textwidth]{images/cern_complex_crop2.png}

\vspace{0.4cm}

* Accelerators are needed to probe high energy physics
* The LHC is the most advanced collider today
  * Challenging to push further the parameters
  * Optimizations require new methods



## Particle Trajectory

\centering
\OldIncludegraphics[width=0.6\textwidth]{./images/closed_orbit.png}

\vspace{0.7cm}

* All particles oscillate around the ring
* Number of transverse oscillations per turn is the tune: $Q_x$ and $Q_y$
    * Fractional part is important! In the LHC often 0.28 and 0.31
* Trajectory is created by magnetics fields and can be disturbed


## Magnets and Optics

\begin{figure}[!htb]
    \captionsetup[subfigure]{labelformat=empty}
    \newlength{\magnetheight}
    \setlength{\magnetheight}{85px}
    \centering
    \begin{subfigure}{0.24\textwidth}
        \includegraphics[height=\magnetheight]{images/magnets/dipole_normal.pdf}
        \caption{
           Dipole
        }
    \end{subfigure}
    \hspace{0.5cm}
    \begin{subfigure}{0.243\textwidth}
        \includegraphics[height=\magnetheight]{images/magnets/quadrupole_normal_f.pdf}
        \caption{
           Quadrupole
        }
    \end{subfigure}
    \hspace{0.5cm}
    \begin{subfigure}{0.243\textwidth}
        \includegraphics[height=\magnetheight]{images/magnets/sextupole_normal.pdf}
        \caption{
           Sextupole
        }
    \end{subfigure}
\end{figure}

* Linear elements
    * Dipoles bend the particles
    * Quadrupoles focus the beam and set the tune
* Non-Linear elements
    * Sextupoles correct particles with a momentum-offset ($\delta$, chromaticity)
    * Octupoles correct tune change with large amplitudes (amp. detuning)
    * Decapoles correct higher-orders chromaticity and amplitude detuning

\centering
\vspace{0.2cm}

Optics: a set of magnet strengths and the related observables




### Resonances {.allowframebreaks}

\centering
\begin{minipage}[l]{.44\textwidth}
  \centering
  \OldIncludegraphics[width=\textwidth]{./images/resonance_diagram_n5.pdf}
\end{minipage}
\hfill
\begin{minipage}[l]{0.44\textwidth}
  \centering
  \OldIncludegraphics[width=\textwidth, trim=0 0 0 130, clip]{./images/b4_correction.pdf}
\end{minipage}

\vspace{0.4cm}

* Resonances lead to unstable motion and increasing amplitudes
    * Goal is to avoid, or at least minimize their effect

* Dynamic Aperture: amplitude particles can reach before being lost
    * Can be measured with lifetime studies


\framebreak

### Resonance Driving Terms

\centering
\OldIncludegraphics[width=0.65\textwidth]{./images/footprint.png}

\vspace{0.2cm}

\small
* RDT $f_{jklm}$: Coefficient linked to a resonance strength
* Example of $f_{1004}$, from decapolar fields
  * Excites resonance $1Q_x - 4Q_y$



## Field Errors

\centering
\hfill
\begin{minipage}[l]{.49\textwidth}
  \centering
  \OldIncludegraphics[height=4.5cm]{./images/dipole_3D.jpg}
\end{minipage}
\hfill
\begin{minipage}[l]{0.49\textwidth}
  \centering
  \OldIncludegraphics[trim=2pt 2pt 2pt 2pt, clip, height=4.5cm]{./images/decapoles_real_pic.jpg}
\end{minipage}
\hfill

\vspace{0.5cm}

* Coils were measured during LHC's construction
    * A magnetic model for errors is then used for simulations
    * Time dependent decay was also measured

\vspace{0.2cm}

* Efforts were done in the past to measure various orders
  * Good understanding of linear and some non-linear errors
  * High-orders only via indirect observables






[//]: -----------------------
[//]:         Thesis
[//]: -----------------------


# Thesis Work

\small

High-order fields will become problematic once we reach higher performances.

Next accelerators like HL-LHC and FCC-ee will be impacted.

\vspace{0.7cm}

* Magnetic error model of decapolar fields seems incomplete
    * Understanding discrepency between simulations and measurements
    * Correcting decapolar fields in operation

\vspace{0.4cm}

* Finding ways to measure higher orders and model them
    * Dodecapoles
    * Decatetrapoles



[//]: -----------------------
[//]:     Decapolar b5
[//]: -----------------------

# Decapolar Studies

::: complete :::


\begin{minipage}[c]{0.3\textwidth}
  \centering
  \OldIncludegraphics[width=1\textwidth]{./images/decapoles_real_pic.jpg}
\end{minipage}
\hfill
\begin{minipage}[c]{0.68\textwidth}
  \centering
  \begin{itemize}
    \small
    \item Large decapolar errors at injection in main edipoles
    \item Current corrections based on magnetic measurements
    \item Correctors every $2^{\text{nd}}$ dipole
  \end{itemize}
\end{minipage}

:::

## Magnetic Model Discrepancy

\centering
\OldIncludegraphics[width=0.7\textwidth]{./images/dq3_corrected_simulation_fidel_legend.pdf}

\small
\vspace{-0.5cm}

$$Q(\delta) = Q_0 + Q'\delta + \frac{1}{2!}Q''\delta^2 + \underbrace{\frac{1}{3!}Q'''\delta^3}_{\text{this one}} + \cdots $$

* Corrections of $Q'''$ based on magnetic measurements
    * Model and measurements off by factor 2, but why?
* Possibles sources:
  * Correctors response
  * Magnetic model



## Checking the Correctors{.allowframebreaks}

\centering
\centering
\OldIncludegraphics[width=0.65\textwidth]{./images/bare_chroma_b1qy_vs_model_legend.png}

\vspace{0.3cm}

* Octupolar and decapolar correctors turned off
* Model and measurements for $Q'''$ are still factor $\approx 2$ off
* Discrepancy still there despite various corrector configurations

\vspace{0.1cm}
 
\normalsize
\begin{center}
  $\rightarrow$ Correctors do not cause the discrepancy
\end{center}



## Chromatic Amplitude Detuning

\centering
\OldIncludegraphics[width=0.7\textwidth]{./images/B2_Qyy_decay0.00.pdf}

\vspace{-.5cm}

\small
$$
  \begin{aligned}
    \Delta Q(J_x, J_y, \delta) = 
    & \frac{\partial^2Q}{\partial J_x \partial \delta}    J_x\delta 
    + \frac{\partial^2 Q}{\partial J_y \partial \delta}   J_y\delta 
    + \frac{1}{3!} \frac{\partial^3 Q}{\partial \delta^3} \delta^3
    \end{aligned}
$$

* Different expression than $Q'''$
* Factor $\approx 2$ compared to simulations again
* First time ever measured in the LHC

\begin{center}
  \normalsize
  $\rightarrow$ Points to an error in our decapolar model, in the arcs 
\end{center}


## Decay in Main Dipoles

\centering
\begin{minipage}[c]{.49\textwidth}
  \begin{figure}
    \OldIncludegraphics[trim=5pt 30pt 0pt 5pt, clip, width=\textwidth]{./images/b5_decay.png}
    \caption*{Change of decapolar component in dipoles over time,\\
              from Field Model documentation\footnotemark}
  \end{figure}
\end{minipage}
\hfill
\begin{minipage}[c]{.49\textwidth}
  \small
  \begin{itemize}
    \item Decapolar decay in the dipoles \\was neglected 15 years ago
    \item Subsequently not integrated in \\magnetic model
    \item Is actually quite large!
  \end{itemize}
\end{minipage}
    

\footnotetext{https://lhc-div-mms.web.cern.ch/tests/MAG/Fidel/}
    
\vspace{0.4cm}

\begin{center}
  \normalsize
  $\rightarrow$ Average decapolar component halved in main dipoles!\\
    Decay is important and needs to be considered
\end{center}


[//]: =================
## Implementation of Decay

\centering
\OldIncludegraphics[width=0.7\textwidth]{./images/B2_Qyy_decay0.47.pdf}

\small 

* Average decapolar decay substracted in simulations
* Most of the difference is now explained
  * Both for $Q'''$ and Chromatic Ampdet.

\begin{center}
  \normalsize
  $\rightarrow$ Discrepancy comes from our error model
\end{center}


## Resonances

### Measuring RDTs

\center
\OldIncludegraphics[width=0.85\textwidth]{./images/ac_dipole_tbt.png}

\vspace{0.2cm}

* The beam is excited by an AC-Dipole
  * Creates large coherent oscillations
  * Improves signal-to-noise ratio
* Quantities like RDTs require high amplitudes
  * Can be challenging to attain due to forced dynamic aperture

\vspace{0.2cm}

\begin{center}
  \small
  $\rightarrow$ Thanks to prior advancements, it is now possible to measure decapolar RDTs!
\end{center}

### Frequency Spectrum

\center
\OldIncludegraphics[width=0.85\textwidth]{./images/spectrum.pdf}

* Several lines are clearly visible
  * AC-Dipole tunes
  * Example of decapolar resonance at $4Q_y$
* Resonance Driving Terms are linked to the line amplitude
  * Normalized to the main line and then fitted over several measurements



### Measurement and Corrections{.allowframebreaks}

\center
\OldIncludegraphics[trim=10pt 0 0 0, clip, width=0.8\textwidth]{./images/rdt_amp_legend.png}

\vspace{0.2cm}

* Corrections based on a response matrix
  * Retrieves the current needed to replicate measurement
* Simultaneous corrections of $f_{1004}$, $Q'''$ and chromatic amp.det.
* First correction of high-orders at injection


### Lifetime Impact of Corrections

\center
\OldIncludegraphics[width=0.95\textwidth]{./images/lifetime.png}

* Clear improvement of lifetime with decapolar correction
* And deterioration with opposite trim

\vspace{0.4cm}

\begin{center}
  \normalsize
  $\rightarrow$ Gain of lifetime at injection energy of $\approx 3\%$
\end{center}


### Other Sources for RDT?
  
\center
\OldIncludegraphics[width=0.8\textwidth]{./images/b5_b4_legend.pdf}

* Unexpected behaviour of the RDT
  * Amplitude seemed to vary every year, even with same configuration
  * Additional octupolar corrections of $Q''$ increased it

\vspace{0.3cm}

\begin{center}
  \normalsize
  $\rightarrow$ Corrections of $Q'''$ not implemented in 2022
\end{center}

### Sextupolar and Octupolar Higher-Order Contributions
  
Via higher-orders of the transfer map,
$e^{:h_1:}e^{:h_2:} = e^{:h:} \quad\quad\quad\quad\quad\quad$
\vspace{0.1cm}

\centering
  \small
  \begin{equation*}
    \begin{alignedat}{3}
      h =& h_1 + h_2  && \Rightarrow \text{1\textsuperscript{st} order}\\
             & + \frac{1}{2} [h_1, h_2]  && \Rightarrow \text{2\textsuperscript{nd} order}\\
             & + \frac{1}{12} [h_1, [h_1, h_2]] \\
             & - \frac{1}{12} [h_2, [h_1, h_2]] \quad && \Rightarrow \text{3\textsuperscript{rd} order}\\
             & + \cdots.
    \end{alignedat}
  \end{equation*}
  
  \vspace{0.1cm}

  \begin{itemize}
    \small
    \item $1^{\text{st}}$ order $\rightarrow$ decapoles
    \item $2^{\text{nd}}$ order $\rightarrow$ sextupoles and octupoles
    \item $3^{\text{rd}}$ order $\rightarrow$ sextupoles together
  \end{itemize}

::: complete :::
\begin{minipage}[l]{0.42\textwidth}
  \centering
  \OldIncludegraphics[width=1\textwidth]{./images/f1004_dq.pdf}
\end{minipage}
:::

\vspace{0.4cm}

\begin{center}
  \normalsize
  $\rightarrow$ Feed-up from sextupoles and octupoles contribute to decapolar RDTs
  Actually never measured before in the LHC!
\end{center}


### Decapolar RDT from Landau Octupoles

\centering
\OldIncludegraphics[width=0.9\textwidth]{./images/MO_f1004_legend_no_MO.png}

\vspace{0.3cm}

* Strong octupoles are used to introduce coherent instabilities damping
* But they increase this RDT by one order of magnitude!

### Landau Octupoles Impact on Lifetime

\centering
\OldIncludegraphics[width=0.95\textwidth]{./images/b5_lifetime.pdf}

\vspace{0.4cm}

* Artificially increased RDT to match expected decapolar impact of sextupoles and octupoles
* Lifetime is negatively impacted by 10%


\begin{center}
  $\rightarrow$ Considering higher-order effects is important
\end{center}


### Forced Dynamic Aperture

\centering
\OldIncludegraphics[width=0.8\textwidth]{./images/losses_with_without_b4b5corr.pdf}

\vspace{0.2cm}

* We now have a good understanding of interplay of fields
* Allows to implemented in operation the new corrections
    * Octupolar ($b_4$) and decapolar ($b_5$)
    * Forced Dynamic Aperture clearly improved

\vspace{0.3cm}

\begin{center}
  \normalsize
  $\rightarrow$ We can now kick higher with the AC-Dipole!
\end{center}


[//]: -----------------------
[//]:          b6
[//]: -----------------------

# Dodecapolar Studies
 
## Dodecapolar RDT $f_{0060}${.allowframebreaks}

\centering
\OldIncludegraphics[width=0.8\textwidth]{images/spectrum_dodecapole_5qy.pdf}

* First measurement made possible this Run
  * Thanks to octupolar ($b_4$) and decapolar ($b_5$) corrections improving DA
  * Never been possible before due to kick amplitudes
* Nice repeatability of measurements

## RDT $f_{0060}$ Modelling

\centering
\begin{minipage}[c]{0.60\textwidth}
  \centering
  \OldIncludegraphics[width=1\textwidth]{images/simulations_f0060.pdf}
\end{minipage}
\hspace{-0.2cm}
\begin{minipage}[c]{0.38\textwidth}
  \centering
  \begin{itemize}
    \small
    \item Dodecapoles ($b_6$) dominate 
    \item Small impact of 
    sextupoles through decapoles ($b_3-b_5$)
  \end{itemize}
\end{minipage}

\vspace{0.4cm}
\begin{center}
  $\rightarrow$ Our model is accurate for this dodecapolar RDT
\end{center}


[//]: -----------------------
[//]:          b7
[//]: -----------------------

# Decatetrapolar Studies

## Chromaticity  {.allowframebreaks}

\centering
\begin{minipage}[c]{0.47\textwidth}
  \centering
  \OldIncludegraphics[width=1\textwidth]{./images/Beam2_Qx.pdf}
\end{minipage}
\begin{minipage}[l]{.03\textwidth}
  \small
  $\rightarrow$
\end{minipage}
\begin{minipage}[c]{0.47\textwidth}
  \centering
  \OldIncludegraphics[width=1\textwidth]{./images/Beam2_Qx_full.pdf}
\end{minipage}

\small

$$Q(\delta) = Q_0 
            + Q'\delta 
            + \frac{1}{2!}Q''\delta^2
            + \frac{1}{3!}Q'''\delta^3 
            + \underbrace{
                \frac{1}{4!}Q^{(4)}\delta^4
              + \frac{1}{5!}Q^{(5)}\delta^5}_{\text{newly measured!}}
            + \cdots
$$

\vspace{-.2cm}

* New measurement technique to increase scan range
* Refined tune cleaning via new processing methods

\begin{center}
  \normalsize
  $\rightarrow$ Clear effects of higher-order chromaticity
\end{center}



::: complete :::

\centering
\OldIncludegraphics[width=0.7\textwidth]{./images/chroma_comparison_B1_X.pdf}

\flushleft
\normalsize
Similar and repeatable measurements achieved

\small

* Over 5 different corrector configurations
* With different optics and years appart

:::

## Decatetrapolar Chromaticity Modelling

\centering
\begin{minipage}[c]{0.6\textwidth}
  \OldIncludegraphics[width=1\textwidth]{./images/q5_ptc.pdf}
\end{minipage}
\hfill
\begin{minipage}[c]{0.37\textwidth}
  \begin{itemize}
    \small
    \item Decatetrapolar ($b_7$) decay has an impact
    \item Some missing sources yet to identify
  \end{itemize}
\end{minipage}

\vspace{0.2cm}
\begin{center}
  \normalsize
  $\rightarrow$ Our model agrees relatively well!
\end{center}


[//]: -----------------------
[//]:       Conclusions
[//]: -----------------------

# Conclusions{.allowframebreaks}

\vspace{0.1cm}

Progressed and achieved first measurements of higher-order fields!

\vspace{0.4cm}

* Decapolar
  * Improved our understanding of decapolar fields and our model
  * Forced DA improved by novel corrections
  * First measurements and corrections of Chromatic Detuning and RDTs

\vspace{0.1cm}

* Dodecapolar
  * First measurement of $f_{0060}$ and benchmark of model

\vspace{0.1cm}

* Decatetrapolar
  * Chromaticity measurements allow to probe up to Decatetrapole

\vspace{0.3cm}

\begin{center}
  \large
  $\rightarrow$ Good first characterization of high orders in the LHC :)
\end{center}

\framebreak

\begin{center}
    Thank you for your attention!
\end{center}
