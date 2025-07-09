def get_bot_response(user_message): 
    user_message = user_message.lower().strip()

    if "hello" in user_message or "hi" in user_message or "hey" in user_message:
        return "Hello! Ask me your Question?"
    elif "define mole and molar mass" in user_message and "co₂" in user_message:
        return "Mole: amount of substance containing 6.022×10²³ particles. Molar mass: mass of one mole of substance. Molecules in 5 moles = 5×6.022×10²³."
    elif "differentiate between empirical formula and molecular formula" in user_message:
        return "A: Empirical: simplest ratio of atoms. Molecular: actual number of atoms in a molecule."
    elif "caco₃" in user_message and "calculate number of ca²⁺ ions" in user_message:
        return "A: Moles = 10g/100g/mol=0.1 mol. Ca²⁺ ions = 0.1×6.022×10²³."
    elif "planck" in user_message and "energy and frequency" in user_message:
        return "A: E=hv (E: energy, h: Planck’s constant, v: frequency)."
    elif "bohr" in user_message and "radius of nth orbit" in user_message:
        return "A: Postulates: (i) electrons in fixed orbits, (ii) quantized energy levels, (iii) energy change during transition. Radius: rₙ=0.529×n²/Z Å."
    elif "chromium" in user_message and "quantum numbers" in user_message:
        return "Write quantum numbers of the last electron of Chromium (Z=24)."
    elif "modern periodic law" in user_message and "atomic size" in user_message:
        return "A: Properties are periodic functions of atomic number. Size decreases across period, increases down group."
    elif "ionization energy" in user_message and "electron affinity" in user_message:
        return "A: Ionization energy ↑ across period, ↓ down group. Electron affinity ↑ across period."
    elif "ie₁" in user_message and "nitrogen" in user_message:
        return "A: Nitrogen has stable half-filled 2p³ configuration, requiring more energy."
    elif "hybridization" in user_message and ("sp³" in user_message or "sp2" in user_message):
        return "A: Mixing of orbitals for bonding. sp³ in CH₄, sp² in C₂H₄."
    elif "lewis structure" in user_message and ("h₂o" in user_message or "nh₃" in user_message):
        return "A: H₂O: bent, 104.5°. NH₃: trigonal pyramidal, 107° due to lone pairs."
    elif "name" in user_message:
        return "I'm a simple chatbot created by you!"
    elif "dipole moment" in user_message and "co₂" in user_message:
        return "A: Dipole moment = charge × distance. CO₂ linear, dipoles cancel."
    elif "ideal gas equation" in user_message and "limitations" in user_message:
        return "A: PV=nRT, valid for ideal gases at low P, high T."
    elif "van der waals" in user_message and "ideal gas behavior" in user_message:
        return "A: (P+a/V²)(V-b)=RT. Corrects for forces (a) and volume (b)."
    elif "boyle" in user_message and "charles" in user_message and "law" in user_message:
        return "A: Boyle’s: P∝1/V (T const). Charles’s: V∝T (P const)."
    elif "first law of thermodynamics" in user_message and "derive ∆u" in user_message:
        return "A: Energy conserved. ∆U (internal energy change)=heat added - work done."
    elif "exothermic" in user_message and "endothermic" in user_message:
        return "A: Exothermic: releases heat (combustion). Endothermic: absorbs heat (photosynthesis)."
    elif "enthalpy" in user_message and "entropy" in user_message and "gibbs free energy" in user_message:
        return "A: Enthalpy: heat content. Entropy: disorder. Gibbs free energy: ∆G=∆H-T∆S."
    elif "kc" in user_message and "kp" in user_message and "derive" in user_message:
        return "A: Kc=[products]/[reactants]. Kp=Kc(RT)^∆n."
    elif "le chatelier" in user_message and "ammonia" in user_message:
        return "A: System shifts to oppose change. For NH₃ formation: ↑P favors products."
    elif "ph" in user_message and "0.01m hcl" in user_message:
        return "A: pH=-log[H⁺]. pH=2 for 0.01M HCl."
    elif "oxidation" in user_message and "reduction" in user_message:
        return "A: Oxidation: e⁻ loss. Reduction: e⁻ gain."
    elif "balance redox" in user_message and "cr₂o₇²⁻" in user_message:
        return "A: Balanced: Cr₂O₇²⁻ + 6Fe²⁺ + 14H⁺ → 2Cr³⁺ + 6Fe³⁺ + 7H₂O."
    elif "disproportionation" in user_message:
        return "A: Same element oxidized & reduced. E.g., Cl₂ + H₂O → HCl + HOCl."
    elif "properties of h₂o and h₂o₂" in user_message:
        return "A: H₂O neutral, H₂O₂ is oxidizer."
    elif "hydrides" in user_message and "classify" in user_message:
        return "A: Ionic (NaH), covalent (CH₄), metallic (TiH₂)."
    elif "uses of heavy water" in user_message:
        return "A: Moderator in nuclear reactors."
    elif "alkali" in user_message and "alkaline earth metals" in user_message:
        return "A: Alkali soft, low MP; alkaline harder."
    elif "anomalous behavior of lithium" in user_message:
        return "A: Small size, covalent bonding."
    elif "becl₂" in user_message and "cacl₂" in user_message:
        return "A: Be²⁺ small, polarizing; Ca²⁺ large, ionic."
    elif "group 13" in user_message:
        return "A: Smaller size, variable oxidation states."
    elif "boron" in user_message and "b³⁺" in user_message:
        return "A: High IE of boron."
    elif "inert pair effect" in user_message:
        return "A: s-electrons inert in heavier p-block (Pb²⁺ more stable)."
    elif "electrophile" in user_message and "nucleophile" in user_message:
        return "A: Electrophile: e⁻ acceptor (H⁺); nucleophile: e⁻ donor (OH⁻)."
    elif "types of organic reactions" in user_message:
        return "A: Substitution, addition, elimination, rearrangement."
    elif "inductive" in user_message and "resonance" in user_message and "hyperconjugation" in user_message:
        return "A: Inductive: e⁻ shift in sigma bonds. Resonance: delocalized pi e⁻. Hyperconjugation: e⁻ from C-H to adjacent pi system."
    elif "markovnikov" in user_message:
        return "A: H⁺ adds to C with more H (e.g., propene + HBr → 2-bromopropane)."
    elif "isomers of c₄h₁₀" in user_message:
        return "A: Butane & isobutane."
    elif "alkanes" in user_message and "alkenes" in user_message and "alkynes" in user_message:
        return "A: Single, double, triple bonds respectively."
    elif "greenhouse gases" in user_message:
        return "A: CO₂, CH₄ trap heat → warming."
    elif "bod" in user_message and "cod" in user_message:
        return " BOD: Measures oxygen needed by bacteria to break down organic waste.COD: Measures oxygen needed to chemically oxidize all waste (organic + inorganic)."
    elif "acid rain" in user_message:
        return "A: SO₂/NOx → acids → damage environment."
    elif "types of unit cells" in user_message:
        return "Unit cells are the smallest repeating units in a crystal lattice. Types: Primitive (corners), Body-Centered (corners + center), Face-Centered (corners + face centers), End-Centered (corners + centers of two opposite faces)."
    elif "packing efficiency" in user_message and ("fcc" in user_message or "bcc" in user_message):
        return "Packing efficiency is the percentage of space occupied by particles. FCC: 74%, BCC: 68%."
    elif "hexagonal close packing" in user_message or "cubic close packing" in user_message:
        return "HCP: ABAB... stacking sequence. CCP: ABCABC... stacking sequence. Difference lies in layer stacking."
    elif "raoult’s law" in user_message:
        return "Raoult's law: partial vapor pressure of a component is proportional to its mole fraction. Applied to find vapor pressure of solutions."
    elif "relative lowering of vapor pressure" in user_message and "molar mass" in user_message:
        return "Relative lowering of vapor pressure (ΔP/P₀) = (n₂/n₁) = (w₂/M₂)/(w₁/M₁). Rearranged: M₂ = (w₂ × M₁ × P₀)/(w₁ × ΔP)."
    elif "abnormal molar masses" in user_message and "van't hoff factor" in user_message:
        return "Abnormal molar masses arise due to association/dissociation. Van't Hoff factor (i) corrects colligative properties: i = observed / calculated."
    elif "nernst equation" in user_message:
        return "Nernst equation: E = E⁰ - (RT/nF) * lnQ. It relates cell potential to concentrations and predicts EMF under non-standard conditions."
    elif "standard electrode potential" in user_message:
        return "Standard electrode potential: potential of a half-cell at standard conditions (1M, 1 atm, 25°C). Used for redox prediction and EMF calculation."
    elif "electrolytic" in user_message and "galvanic cells" in user_message:
        return "Electrolytic cells: non-spontaneous, need electricity. Galvanic cells: spontaneous, produce electricity."
    elif "order" in user_message and "molecularity" in user_message:
        return "Order: sum of powers of concentrations in rate law (experimental). Molecularity: number of colliding molecules in an elementary step (theoretical)."
    elif "integrated rate equations" in user_message and ("first" in user_message or "second" in user_message):
        return "First-order: ln[A] = -kt + ln[A]₀. Second-order: 1/[A] = kt + 1/[A]₀."
    elif "arrhenius equation" in user_message and "activation energy" in user_message:
        return "Arrhenius: k = A * e^(-Ea/RT), where Ea is activation energy. It shows temperature dependence of rate constant."
    elif "types of adsorption" in user_message:
        return "Physisorption: weak van der Waals forces, e.g., gases on charcoal. Chemisorption: strong chemical bonds, e.g., H2 on Ni."
    elif "emulsions" in user_message:
        return "Emulsions: colloidal mixtures of two immiscible liquids. Types: oil-in-water (milk), water-in-oil (butter). Used in food, cosmetics, pharma."
    elif "enzyme catalysis" in user_message:
        return "Enzymes form enzyme-substrate complexes, lower activation energy, and increase reaction speed. Highly specific."
     # General Principles and Processes of Isolation of Elements
    if "Describe the extraction of aluminum from bauxite ore" in user_message:
        return "Aluminum is extracted from bauxite ore by Bayer’s process to produce alumina, then electrolyzed (Hall-Heroult process) to obtain pure aluminum."
    elif "Explain the froth flotation process with diagrams" in user_message:
        return "Froth flotation separates sulfide ores from gangue by using collectors and frothers to produce a froth of ore particles that can be skimmed off."
    elif "What is zone refining? State its significance" in user_message:
        return "Zone refining involves moving a molten zone along a solid rod to purify metals. It removes impurities and is essential for semiconductor production."

    # The p-Block Elements
    elif "Discuss the anomalous behaviour of nitrogen" in user_message:
        return "Nitrogen shows anomalous behavior due to its small size, high electronegativity, high ionization energy, and lack of d-orbitals."
    elif "Explain the structure of PCl5 and SF6" in user_message:
        return "PCl5 has a trigonal bipyramidal structure; SF6 has an octahedral structure."
    elif "Write the preparation and properties of ammonia and nitric acid" in user_message:
        return "Ammonia: Haber process, basic and reducing. Nitric acid: Ostwald process, strong acid, oxidizing agent."

    # The d- and f-Block Elements
    elif "Explain the lanthanide contraction and its consequences" in user_message:
        return "Lanthanide contraction is the steady decrease in size of lanthanides due to poor shielding of f-electrons. It causes similar properties of 4d and 5d elements."
    elif "Discuss the oxidation states of transition elements" in user_message:
        return "Transition elements exhibit variable oxidation states due to similar energies of ns and (n-1)d electrons."
    elif "What are interstitial compounds? Give examples" in user_message:
        return "Interstitial compounds form when small atoms occupy spaces in metal lattices. Examples: TiC, Fe3H."

    # Coordination Compounds
    elif "Explain Werner’s theory of coordination compounds" in user_message:
        return "Werner’s theory distinguishes primary valency (ionizable) and secondary valency (coordination number) to explain coordination compound structures."
    elif "Discuss the isomerism shown by coordination compounds" in user_message:
        return "Coordination compounds show structural isomerism (ionization, linkage, coordination) and stereoisomerism (geometrical and optical)."
    elif "What is crystal field theory? Discuss for octahedral complexes" in user_message:
        return "Crystal field theory explains d-orbital splitting in ligand fields. In octahedral complexes, it splits into t2g (low) and eg (high) levels."

    # Haloalkanes and Haloarenes
    elif "Explain the SN1 and SN2 mechanisms with examples" in user_message:
        return "SN1: two-step, carbocation intermediate (e.g., tert-butyl bromide). SN2: one-step, backside attack (e.g., methyl bromide with OH⁻)."
    elif "Discuss the preparation of haloalkanes from alcohols" in user_message:
        return "Alcohols react with HX, PX3, or SOCl2 to form haloalkanes by nucleophilic substitution."
    elif "What are the environmental effects of CFCs" in user_message:
        return "CFCs deplete the ozone layer, leading to increased UV radiation reaching Earth’s surface."

    # Alcohols, Phenols and Ethers
    elif "Discuss the acidic nature of phenol" in user_message:
        return "Phenol is more acidic than alcohols due to resonance stabilization of the phenoxide ion."
    elif "Write the reactions of alcohols with Lucas reagent" in user_message:
        return "Lucas reagent tests alcohols’ reactivity: tertiary > secondary > primary, forming alkyl chlorides."
    elif "Explain the Williamson ether synthesis" in user_message:
        return "Williamson ether synthesis: reaction of sodium alkoxide with a primary alkyl halide to make ethers."

    # Aldehydes, Ketones and Carboxylic Acids
    elif "Discuss the nucleophilic addition reactions of aldehydes and ketones" in user_message:
        return "Aldehydes and ketones undergo nucleophilic addition with nucleophiles like HCN, NaHSO3, and ammonia derivatives."
    elif "What is Cannizzaro reaction? Explain with mechanism" in user_message:
        return "Cannizzaro reaction: aldehydes without alpha-hydrogen undergo redox to give one alcohol and one carboxylic acid."
    elif "Explain the acidity of carboxylic acids" in user_message:
        return "Carboxylic acids are acidic due to resonance stabilization of the carboxylate ion and electron withdrawing effects."

    # Amines
    elif "Explain the Hoffmann bromamide reaction" in user_message:
        return "Hoffmann bromamide reaction: primary amide reacts with Br2 and NaOH to give primary amine via rearrangement."
    elif "Discuss the basicity of amines in aqueous solution" in user_message:
        return "Amines’ basicity depends on electron availability on nitrogen; aliphatic amines are more basic than aromatic amines."
    elif "What is diazotization? Give its significance" in user_message:
        return "Diazotization: primary aromatic amines react with nitrous acid to form diazonium salts, useful in dye synthesis."

    # Biomolecules
    elif "What are enzymes? Discuss their mechanism of action" in user_message:
        return "Enzymes are biocatalysts. They form enzyme-substrate complexes, lowering activation energy and increasing reaction rates."
    elif "Explain the structure of proteins and types" in user_message:
        return "Proteins: primary (sequence), secondary (α-helix, β-sheet), tertiary (3D folding), quaternary (multi-subunit structures)."
    elif "Discuss the classification of carbohydrates" in user_message:
        return "Carbohydrates: monosaccharides (glucose), oligosaccharides (sucrose), polysaccharides (starch, cellulose)."

    # Polymers
    elif "Explain the types of polymers with examples" in user_message:
        return "Types: addition (polyethylene), condensation (nylon, terylene), copolymers (Buna-S)."
    elif "What is condensation polymerization? Give examples" in user_message:
        return "Condensation polymerization involves loss of small molecules (e.g., H2O) to form polymers like nylon-6,6."
    elif "Discuss the structure and uses of bakelite and nylon" in user_message:
        return "Bakelite: thermosetting resin for electrical goods. Nylon: synthetic fiber for textiles and ropes."

    # Chemistry in Everyday Life
    elif "Explain the role of drugs as analgesics and antipyretics" in user_message:
        return "Analgesics relieve pain (e.g., aspirin); antipyretics reduce fever (e.g., paracetamol). Both block prostaglandin synthesis."
    elif "Discuss the cleansing action of soaps and detergents" in user_message:
        return "Soaps/detergents form micelles that trap dirt/oil, making them soluble in water."
    elif "What are food preservatives? Give examples" in user_message:
        return "Food preservatives prevent spoilage by microbes. Examples: sodium benzoate, sodium metabisulfite."
# physics 11th
    # Chapter: Physical World
    if "scope and excitement" in user_message:
        return "A: Physics explores natural phenomena and how they connect to our daily lives."
    elif "relationship of physics with technology" in user_message:
        return "A: Physics helps develop technology and improves our understanding of the universe."
    elif "fundamental forces" in user_message:
        return "A: Gravitational, electromagnetic, strong nuclear, and weak nuclear forces."

    # Chapter: Units and Measurements
    elif "si units" in user_message:
        return "A: Standardized units like meter, kilogram, second, etc., used globally."
    elif "dimensional analysis" in user_message:
        return "A: Used to check equation correctness by comparing dimensions."
    elif "significant figures" in user_message:
        return "A: Digits that carry meaning, showing measurement precision."

    # Chapter: Motion in a Straight Line
    elif "distance and displacement" in user_message:
        return "A: Distance is total path length, displacement is shortest path."
    elif "equations of motion" in user_message:
        return "A: v = u + at, s = ut + 0.5at², v² = u² + 2as."
    elif "relative velocity" in user_message:
        return "A: Velocity of one object with respect to another."

    # Chapter: Motion in a Plane
    elif "vector addition" in user_message:
        return "A: Combining vectors using head-to-tail or parallelogram method."
    elif "projectile motion" in user_message:
        return "A: Motion under gravity; horizontal & vertical motions are independent."
    elif "uniform circular motion" in user_message:
        return "A: Motion in a circle at constant speed."

    # Chapter: Laws of Motion
    elif "newton's three laws" in user_message:
        return "A: Law of inertia, F=ma, action-reaction pairs."
    elif "law of conservation of momentum" in user_message:
        return "A: Total momentum remains constant in absence of external forces."
    elif "friction" in user_message:
        return "A: Force resisting motion, static and kinetic types."

    # Chapter: Work, Energy and Power
    elif "work-energy theorem" in user_message:
        return "A: Work done equals change in kinetic energy."
    elif "kinetic and potential energy" in user_message:
        return "A: Kinetic energy = 0.5mv², potential energy depends on position."
    elif "power" in user_message:
        return "A: Rate of doing work, P = W/t."

    # Chapter: System of Particles and Rotational Motion
    elif "center of mass" in user_message:
        return "A: Point representing whole mass distribution."
    elif "torque and angular momentum" in user_message:
        return "A: Torque is rotational force, angular momentum is rotational analog of momentum."
    elif "moment of inertia" in user_message:
        return "A: Resistance to rotational motion, depends on mass distribution."

    # Chapter: Gravitation
    elif "newton's law of gravitation" in user_message:
        return "A: F = G(m1m2)/r², force of attraction between masses."
    elif "acceleration due to gravity" in user_message:
        return "A: g = 9.8 m/s² on Earth, varies with altitude & latitude."
    elif "escape velocity" in user_message:
        return "A: Velocity to escape gravity, vₑ = √(2GM/R)."

    # Chapter: Mechanical Properties of Solids
    elif "stress and strain" in user_message:
        return "A: Stress = F/A, strain = ΔL/L₀."
    elif "hooke's law" in user_message:
        return "A: Stress ∝ strain for elastic limit."
    elif "elastic modulus" in user_message:
        return "A: Ratio of stress to strain for solids (Young's, bulk, shear)."

    # Chapter: Mechanical Properties of Fluids
    elif "pressure in fluids" in user_message:
        return "A: P = F/A, measured in Pascal."
    elif "pascal's law" in user_message:
        return "A: Pressure applied to fluid transmits equally in all directions."
    elif "viscosity and surface tension" in user_message:
        return "A: Viscosity resists flow; surface tension causes liquids to minimize area."

    # Chapter: Thermal Properties of Matter
    elif "heat capacity" in user_message:
        return "A: Amount of heat to raise temperature by 1°C."
    elif "thermal expansion" in user_message:
        return "A: Increase in volume/length with temperature."
    elif "heat transfer" in user_message:
        return "A: Conduction, convection, radiation."

    # Chapter: Thermodynamics
    elif "first law of thermodynamics" in user_message:
        return "A: ΔU = Q - W, conservation of energy."
    elif "isothermal and adiabatic" in user_message:
        return "A: Isothermal: T constant; adiabatic: no heat exchange."
    elif "entropy and second law" in user_message:
        return "A: Entropy measures disorder; second law: entropy increases."

    # Chapter: Kinetic Theory
    elif "kinetic theory of gases" in user_message:
        return "A: Assumes gas particles in random motion, collisions elastic."
    elif "pressure of ideal gas" in user_message:
        return "A: P = 1/3 ρv² for kinetic theory."
    elif "mean free path" in user_message:
        return "A: Average distance between collisions."

    # Chapter: Oscillations
    elif "simple harmonic motion" in user_message:
        return "A: Restoring force ∝ displacement, sinusoidal motion."
    elif "simple pendulum" in user_message:
        return "A: T = 2π√(l/g), period depends on length & g."
    elif "damping and resonance" in user_message:
        return "A: Damping reduces amplitude; resonance: max amplitude at natural frequency."

    # Chapter: Waves
    elif "transverse and longitudinal waves" in user_message:
        return "A: Transverse: perpendicular vibrations; longitudinal: parallel."
    elif "superposition of waves" in user_message:
        return "A: Waves add algebraically, can interfere constructively/destructively."
    elif "standing waves and resonance" in user_message:
        return "A: Nodes & antinodes form; resonance when driving frequency matches natural frequency."
   
    else:
        return "I don't have an answer for that right now. Can you ask me something else?"
