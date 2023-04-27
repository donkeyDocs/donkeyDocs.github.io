# Donkey Docs

Meant to be a repository of my notes on various subjects I have studied over the years—hence the title. 😂 

The best way to reach me is by email.

<sub> [ atul.singh.arora@gmail.com | asarora@caltech.edu ] </sub>



## Introduction to Cryptography

Based on the textbook by Katz and Lindell

|a | b |
| - | - |
|c | d|  


<details open>
<summary>

### Quantum Depth in the Random Oracle Model

*Atul Singh Arora, Andrea Coladangelo, Matthew Coudron, Alexandru Gheorghiu, Uttam Singh, Hendrik Waldner*

<sub> Oct 2022 [ [arXiv](https://arxiv.org/abs/2210.06454) | [GitHub](https://atulsingharora.github.io/instaDepth) ] —— [ [STOC '23](http://acm-stoc.org/stoc2023/accepted.html) ]  </sub>  
<sub>104 pages (+9 page Appendix), 10 figures
</summary>

> We give a comprehensive characterisation of the computational power of shallow quantum circuits combined with classical computation. Specifically, for classes of search problems, we show that the following statements hold, relative to a random oracle:  
(a) $\mathsf{BPP}^{\mathsf{QNC}^{\mathsf{BPP}}} \neq \mathsf{BQP}$. This refutes Jozsa's conjecture [QIP 05] in the random oracle model. As a result, this gives the first instantiatable separation between the classes by replacing the oracle with a cryptographic hash function, yielding a resolution to one of Aaronson's ten semi-grand challenges in quantum computing.  
(b) $\mathsf{BPP}^{\mathsf{QNC}} \nsubseteq \mathsf{QNC}^{\mathsf{BPP}}$ and $\mathsf{QNC}^{\mathsf{BPP}} \nsubseteq \mathsf{BPP}^{\mathsf{QNC}}$. This shows that there is a subtle interplay between classical computation and shallow quantum computation. In fact, for the second separation, we establish that, for some problems, the ability to perform adaptive measurements in a single shallow quantum circuit, is more useful than the ability to perform polynomially many shallow quantum circuits without adaptive measurements.  
(c) There exists a 2-message proof of quantum depth protocol. Such a protocol allows a classical verifier to efficiently certify that a prover must be performing a computation of some minimum quantum depth. Our proof of quantum depth can be instantiated using the recent proof of quantumness construction by Yamakawa and Zhandry [FOCS 22].

</details>


<details>
<summary>

### Solutions to Quantum Weak Coin Flipping
 (Consolidation of all our previous results about weak coin flipping into a single journal version)  
*Atul Singh Arora, Jérémie Roland, Chrysoula Vlachou, Stephan Weis*

<sub> Aug 2022 [ [ePrint](https://eprint.iacr.org/2022/1101) ] —— [preparing to submit]  </sub>  
<sub> 110 + 28 pages, 24 figures</sub>

</summary>

> Weak coin flipping is an important cryptographic primitive, as it is the strongest known secure two-party computation primitive, that classically becomes secure only when certain assumptions are made (e.g. computational hardness), while quantumly there exist protocols that achieve arbitrarily close to perfect security. This breakthrough result was established by C. Mochon in 2007 [arXiv:0711.4114], however, his proof of existence was partially non-constructive, thus, setting back the proposal of explicit protocols. In this work, we report three different solutions to the quantum weak coin flipping problem. In particular, we propose different methods that result---either analytically or numerically---in the operators needed to construct weak coin flipping protocols with different levels of security, including nearly perfect security. In order to develop these methods, we study the quantum weak coin flipping problem from both an algebraic and a geometric perspective. We also analytically construct illustrative examples of weak coin flipping protocols achieving different levels of security.

</details>


<details>
<summary>

### Self-Testing of a Single Quantum System: Theory and Experiment
*Xiao-Min Hu, Yi Xie, Atul Singh Arora, Ming-Zhong Ai, Kishor Bharti, Jie Zhang, Wei Wu, Ping-Xing Chen, Jin-Ming Cui, Bi-Heng Liu, Yun-Feng Huang, Chuan-Feng Li, Guang-Can Guo, Jérémie Roland, Adán Cabello, Leong-Chuan Kwek*

<sub> Mar 2022 [ [arXiv](https://arxiv.org/abs/2203.09003) ] —— [preparing to submit]  </sub>  
<sub>19+6 pages, 2+1 figures</sub>
</summary>

> Self-testing allows for characterising quantum systems under minimal assumptions.
However, existing schemes rely on quantum non-locality and cannot be applied to systems that are not entangled. Here, we introduce a robust method that achieves self-testing of individual systems by taking advantage of contextuality. The scheme is based on the simplest contextuality witness for the simplest contextual quantum system---the Klyachko-Can-Binicioğlu-Shumovsky inequality for the qutrit. We establish a lower bound on the fidelity of the state and the measurements as a function of the value of the witness under a pragmatic assumption on the measurements. We apply the method in an experiment on a single trapped $^{40}{\rm Ca}^+$ and using randomly chosen measurements and perfect detection efficiency. Using the observed statistics, we obtain the first experimental demonstration of self-testing of a single quantum system with negligible deviations from the assumptions.
</details>




<details>
<summary>

### Oracle separations of hybrid quantum-classical circuits
*Atul Singh Arora, Alexandru Gheorghiu, Uttam Singh*

<sub> Jan 2022 [ [arXiv](https://arxiv.org/abs/2201.01904) | [GitHub](https://atulsingharora.github.io/HQC) ] —— [submitted]  </sub>  
<sub>47 pages, 5 figures</sub>

</summary>

> An important theoretical problem in the study of quantum computation, that is also practically relevant in the context of near-term quantum devices, is to understand the computational power of hybrid models, that combine polynomial-time classical computation with short-depth quantum computation. Here, we consider two such models: CQ_d which captures the scenario of a polynomial-time classical algorithm that queries a d-depth quantum computer many times; and QC_d which is more analogous to measurement-based quantum computation and captures the scenario of a d-depth quantum computer with the ability to change the sequence of gates being applied depending on measurement outcomes processed by a classical computation. Chia, Chung and Lai (STOC 2020) and Coudron and Menda (STOC 2020) showed that these models (with d=polylog(n)) are strictly weaker than BQP (the class of problems solvable by polynomial-time quantum computation), relative to an oracle, disproving a conjecture of Jozsa in the relativised world.  
In this paper, we show that, despite the similarities between CQ_d and QC_d, the two models are incomparable, i.e. CQ_d ⊈ QC_d and QC_d ⊈ CQ_d relative to an oracle. In other words, we show that there exist problems that one model can solve but not the other and vice versa. We do this by considering new oracle problems that capture the distinctions between the two models and by introducing the notion of an intrinsically stochastic oracle, an oracle whose responses are inherently randomised, which is used for our second result. While we leave showing the second separation relative to a standard oracle as an open problem, we believe the notion of stochastic oracles could be of independent interest for studying complexity classes which have resisted separation in the standard oracle model. Our constructions also yield simpler oracle separations between the hybrid models and BQP, compared to earlier works.

</details>


<details>
<summary>

### Improving the security of device independent weak coin flipping protocols
*Atul Singh Arora, Jamie Sikora, Tom Van Himbeeck*

 <sub> Oct 2021 [ [overleaf](https://www.overleaf.com/read/jhwnvgbntqkd) ] —— [finalising preparation]  </sub>  
<sub> 21 + 1 pages, 3 figures </sub>

</summary> 

> Weak coin flipping is the cryptographic task where Alice and Bob remotely flip a coin but want opposite outcomes. 
This work studies this task in the device-independent regime where Alice and Bob neither trust each other, nor their quantum devices. 
The best protocol was devised ten years ago by Silman, Chailloux, Aharon, Kerenidis, Pironio, and Massar with bias $\epsilon \le 0.33664$, where the bias is a commonly adopted security measure for coin flipping protocols. 
This work presents some techniques to lower the bias of device-independent weak coin flipping protocols, namely self-testing and abort-phobic compositions. 
By applying these techniques to the SCAKPM '11 protocol above, we are able to lower the bias to $\epsilon \approx 0.31486$ and assuming a continuity conjecture, we can suppress it further to $\epsilon \approx 0.29104$. 
In our analysis, we show how to harness the rigidity bounds for the GHZ game in our setting and examine the continuity of an optimisation problem to bound the bias, which may be of independent interest.  

</details>


<details>
<summary>

### Analytic quantum weak coin flipping protocols with arbitrarily small bias
*Atul Singh Arora, Jérémie Roland, Chrysoula Vlachou*

<sub> 13 July 2020 [ [arXiv](https://arxiv.org/abs/1911.13283) | [GitHub](https://atulsingharora.github.io/WCF2) ] —— [ [SODA '21](), QIP '21, QCrypt '21 ] </sub>  
<sub>13+14 pages, 3 figures</sub>
</summary>

> Weak coin flipping (WCF) is a fundamental cryptographic primitive for two-party secure computation, where two distrustful parties need to remotely establish a shared random bit whilst having opposite preferred outcomes. It is the strongest known primitive with arbitrarily close to perfect security quantumly while classically, its security is completely compromised (unless one makes further assumptions, such as computational hardness).  A WCF protocol is said to have bias $\epsilon$ if neither party can force their preferred outcome with probability greater than $1/2+\epsilon$. Classical WCF protocols are shown to have bias $1/2$, i.e., a cheating party can always force their preferred outcome. On the other hand, there exist quantum WCF protocols with arbitrarily small bias, as Mochon showed in his seminal work in 2007 [arXiv:0711.4114]. In particular, he proved the existence of a family of WCF protocols approaching bias $\epsilon (k)=1/(4k+2)$ for arbitrarily large $k$ and proposed a protocol with bias $1/6$. Last year, Arora, Roland and Weis presented a protocol with bias $1/10$ and to go below this bias, they designed an algorithm that *numerically* constructs unitary matrices corresponding to WCF protocols with arbitrarily small bias [STOC'19, p.205-216]. In this work, we present new techniques which yield a fully analytical construction of WCF protocols with bias arbitrarily close to zero, thus achieving a solution that has been missing for more than a decade. Furthermore, our new techniques lead to a simplified proof of existence of WCF protocols by circumventing the non-constructive part of Mochon's proof. As an example, we illustrate the construction of a WCF protocol with bias $1/14$.

</details>

<details>
<summary>

### All fundamental non-contextuality inequalities are unique
*Kishor Bharti, Atul Singh Arora, Leong Chuan Kwek, Jérémie Roland*

<sub> Dec 2019 [ [arXiv](https://arxiv.org/abs/1811.05294) ] —— [ [Phys Rev Res 2020](https://doi.org/10.1103/PhysRevResearch.2.033010) ]
 </sub>  
<sub>17 pages (5 main, 12 appendix), 4 figures</sub>

</summary>

> Contextuality is one way of capturing the non-classicality of quantum theory. The contextual nature of a theory is often witnessed via the violation of non-contextuality inequalities---certain linear inequalities involving probabilities of measurement events. Using the exclusivity graph approach (one of the two main graph theoretic approaches for studying contextuality), it was shown [PRA 88, 032104 (2013); Annals of mathematics, 51-299 (2006)] that a necessary and sufficient condition for witnessing contextuality is the presence of an odd number of events (greater than three) which are either cyclically or anti-cyclically exclusive. Thus, the non-contextuality inequalities whose underlying exclusivity structure is as stated, either cyclic or anti-cyclic, are fundamental to quantum theory. We show that there is a unique non-contextuality inequality for each non-trivial cycle and anti-cycle. In addition to the foundational interest, we expect this to aid the understanding of contextuality as a resource to quantum computing and its applications to local self-testing.

</details>


<details>
<summary>

### Quantum Weak Coin Flipping
*Atul Singh Arora, Jérémie Roland, Stephan Weis*

<sub> Nov 2018 [ [arXiv](https://arxiv.org/abs/1811.02984) | [GitHub](https://atulsingharora.github.io/WCF) ] —— 
[ [STOC '19](https://doi.org/10.1145/3313276.3316306), QIP '19 ]  
98 pages, split into 3 parts, 10 figures
</sub>

</summary>

> We investigate weak coin flipping, a fundamental cryptographic primitive where two distrustful parties need to remotely establish a shared random bit. A cheating player can try to bias the output bit towards a preferred value. For weak coin flipping the players have known opposite preferred values. A weak coin-flipping protocol has a bias $\epsilon$ if neither player can force the outcome towards his/her preferred value with probability more than $\frac{1}{2}+\epsilon$. While it is known that classically $\epsilon=\frac{1}{2}$, Mochon showed in 2007 that quantumly weak coin flipping can be achieved with arbitrarily small bias (near perfect) but the best known explicit protocol has bias $\frac{1}{6}$ (also due to Mochon, 2005). We propose a framework to construct new explicit protocols achieving biases below $\frac{1}{6}$. In particular, we construct explicit unitaries for protocols with bias up to $\frac{1}{10}$. To go below, we introduce what we call the Elliptic Monotone Align (EMA) algorithm which, together with the framework, allows us to numerically construct protocols with arbitrarily small biases.
</details>


<details>
<summary>

### Revisiting the admissibility of non-contextual hidden variable models in quantum mechanics

*Atul Singh Arora, Kishor Bharti, Arvind*

<sub> Nov 2018 [ [arXiv](https://arxiv.org/abs/1607.03498) ] —— 
[ [Phys Lett A, 2018](https://doi.org/10.1016/j.physleta.2018.11.049) ]   
4 pages, 1 figure
</sub>

</summary>

> We construct a non-contextual hidden variable model consistent with all the kinematic predictions of quantum mechanics (QM). The famous Bell-KS theorem shows that non-contextual models which satisfy a further reasonable restriction are inconsistent with QM. In our construction, we define a weaker variant of this restriction which captures its essence while still allowing a non-contextual description of QM. This is in contrast to the contextual hidden variable toy models, such as the one by Bell, and brings out an interesting alternate way of looking at QM. The results also relate to the Bohmian model, where it is harder to pin down such features.

</details>


<details>
<summary>

### Proposal for a macroscopic test of local realism with phase-space measurements

*Atul Singh Arora, Ali Asadian*

<sub> Aug 2015 [ [arXiv](https://arxiv.org/abs/1508.04588)  ] —— 
[ [Phys Rev A, 2015](https://doi.org/10.1103/PhysRevA.92.062107) ]  
9 pages, 3 figures
</sub>

</summary>

> We propose a new test of local realism based on correlation measurements of continuum valued functions of positions and momenta, known as modular variables. The Wigner representation of these observables are bounded in phase space, and therefore, the associated inequality holds for any state described by a non-negative Wigner function. This agrees with Bell's remark that positive Wigner functions, serving as a valid probability distribution over local (hidden) phase space coordinates, do not reveal non-locality. We construct a class of entangled states resulting in a violation of the inequality, and thus truly demonstrate non-locality in phase space. The states can be realized through grating techniques in space-like separated interferometric setups. The non-locality is verified from the spatial correlation data, collected from the screens.

</details>

⟨ [list of publications on arXiv](https://arxiv.org/search/quant-ph?searchtype=author&query=Arora%2C+A+S) ⟩

