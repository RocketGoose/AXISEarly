# AXISE: Another Xtreme Industry Set Early

A fork of AXIS for those who like to start the game early. 

To Do:
    - [x] Intro dates for Steelcity 
    - [] Intro dates for Tropical Paradise

# AXIS: Another Xtreme Industry Set

A fork of FIRS 4.4.0 by andythenorth. The official successor to XIS: Xtreme Industry Set.

## Table of contents

- 1.0 [Overview](#10-overview)
- 2.0 [Economies](#20-economies)
- 3.0 [Source code](#30-source-code)
- 4.0 [Developer Notices](#40-developer-notices)
- 5.0 [Credits](#50-credits)

## 1.0 Overview

AXIS is an industry set for OpenTTD. 

If you are familiar with FIRS, you will also be familiar with AXIS because the game mechanics are largely unchanged. However, AXIS has much bigger, broader and more complex economies than FIRS. 

Using JGR Patch Pack is highly recommended, though not required. AXIS is best played with cargodist (asymmetric equal distribution) enabled for all cargos, and cargo delivery distribution mode set to Balanced. 

Using compatible vehicle NewGRFs is also highly recommended, but not required in recent versions of OpenTTD. 

## 2.0 Economies

Currently, there are two complete economies; Steel City and Tropical Paradise.

Steel City is based on FIRS's Steeltown economy, but it replaces FIRS's reliance on "magic ports" with full-fledged industry chains including a complex petrochemical chain, and new specialised factories for things such as cleaning agents and electrical machines. There is also an improved agricultural chain, but it is not the main focus of this economy.

Steel City is suitable for representing any region that is heavily industrialised with a focus on steel production. Examples include Japan, China, Germany and the Northeast USA.

Tropical Paradise is not based on any specific FIRS economy, but it incorporates elements from FIRS's In A Hot Country and Tropic Basic economies, among others. Unlike the FIRS tropical economies, AXIS Tropical Paradise is a fully integrated economy with a focus on heavy agricultural industry, as well as resource extraction and manufacturing. 

Tropical Paradise is suitable for representing industrialised regions in tropical or subtropical areas. Examples include India, Southeast Asia and parts of South Africa and South America.

## 3.0 Source code

The source code is available on GitHub (https://github.com/EmperorJake/AXIS)

To compile, follow the instructions to compile FIRS.

Translations are welcome. Please pay attention to the new strings added in AXIS, and strings which are similar to, but changed from FIRS.

## 4.0 Developer Notices

All AXIS economies use all 64 cargo type slots, therefore it is incompatible with any other NewGRF that defines any cargo types. 

AXIS adds a few new cargo types that are not present in FIRS, but cargolabels ensure compatibility with most modern vehicle sets.

## 5.0 Credits & License

Coding & Concept: Emperor Jake <br/>
Based on code by andythenorth et al.

Graphics by the FIRS team, with additions by Emperor Jake and GarryG.

Special thanks to: Tintinfan, Romazoon, Erato, Azusa, and everyone else who played on Tin's server

All content is licensed under [GPL v2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
