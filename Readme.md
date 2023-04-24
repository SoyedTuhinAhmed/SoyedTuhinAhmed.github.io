<!DOCTYPE html>
<html>
<head>
	<title>Soyed Tuhin Ahmed - Research Profile</title>
	<style>
		/* style for navbar */
		.navbar {
			overflow: hidden;
			background-color: #333;
			position: sticky;
			top: 0;
		}

		/* style for navbar links */
		.navbar a {
			float: left;
			display: block;
			color: #f2f2f2;
			text-align: center;
			padding: 14px 16px;
			text-decoration: none;
			font-size: 17px;
		}

		/* style for active navbar link */
		.active {
			background-color: #4CAF50;
			color: white;
		}
	</style>
</head>
<body>
	<!-- navbar -->
	<div class="navbar">
		<a class="active" href="#about-me">About Me</a>
		<a href="#awards-and-nomination">Awards and Nomination</a>
		<a href="#research-projects">Research Projects</a>
		<a href="#research-statement">Research Statement</a>
		<a href="#publications">Publications</a>
		<a href="#contact">Contact</a>
	</div>

	<!-- content -->
	<img align="left" src="tuhin_.jpg" width="120" height="120">

	<h2 id="about-me">About Me</h2>
	<p>I am a PhD student in computer science at KIT - Karlsruhe Institute of Technology, Karlsruhe, Germany at the Chair of Dependable Nano Computing (CDNC), working under the supervision of Prof. Dr. Mehdi B. Tahoori. My research interests include neuromorphic computing, resilient hardware accelerator for machine learning, robust and accurate deep learning, hardware architectures for neural network applications, computation in memory, and emerging memory computing paradigms.</p>

	<h2 id="awards-and-nomination">Awards and Nomination</h2>
	<ul>
		<li>Richard Newton Fellowship at DAC 2022</li>
		<li>Summa-Cum-Laude and university gold medal from Amarican International University Bangladesh (AIUB), 2016</li>
		<li>Academic Merit Scholarship from Amarican International University Bangladesh (AIUB), 2013-2015</li>
		<li>EIT Digital Scholarships, entry at KTH Royal Institute of Technology, Sweden, 2016 (did not pursue)</li>
		<li>Marie Curie Fellowship from University of York, UK, 2022, (did not pursue)</li>
		<li>Several best paper nominations, see below</li>
	</ul>

	<h2 id="research-projects">Research Projects</h2>
	<ul>
		<li>NeuSPIN – An ANR project: NeuSPIN stands for Design of a reliable edge neuromorphic system based on spintronics for Green AI <a href="https://www.spintec.fr/neuspin-an-anr-project/">[Link]</a></li>
	</ul>

	<h2 id="research-statement">Neuromorphic Computing and Deep Learning Research Overview</h2>
	<p>My research is in the field of robust and efficient algorithms for neuromorphic computing with emerging resistive NVM memories (e.g., spintronics), fault tolerance, testing, and uncertainty estimation. The primary aim is to develop efficient and robust neuromorphic systems, addressing challenges to a trustworthy deep learning system with uncertainty estimation, fault tolerance, and testability with an algorithm-hardware co-design approach. For a detailed research statement, please refer to <a href="ResearchStatement.md">ResearchStatement</a>.</p>

    
h2>Publications</h2>

<h3>Journals</h3>

<ol>
<li><a href="#">[J1] S. T. Ahmed, et al., NeuroScrub+: Mitigating Retention Faults Using Flexible Approximate Scrubbing in Neuromorphic Fabric Based on Resistive Memories, IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2022.</a></li>
<li><a href="#">[J2] S. T. Ahmed, et al., SpinDrop: Dropout-Based Bayesian Binary Neural Networks with spintronic Implementation, IEEE Journal on Emerging and Selected Topics in Circuits and Systems, 2023.</a></li>
<li><a href="#">[J3] S. T. Ahmed, et al., Fault-tolerant Neuromorphic Computing with Memristors Using Functional ATPG for Efficient Re-calibration, IEEE Design and Test, 2023, [Revised Publication for Top Picks in VTS 2022].</a></li>
<li><a href="#">[J4] S. T. Ahmed, et al., Design-Time Reference Current Generation for Robust Spintronic-Based Neuromorphic Architecture, ACM Journal on Emerging Technologies in Computing Systems, 2023, [Under Review].</a></li>
<li><a href="#">[J5] S. T. Ahmed, et al., Algorithm-Hardware Co-Design for Uncertainty Estimation on Spintronic-Based Architectures, Esweek 2023/ACM Transactions on Embedded Computing System [Under Review, generic title used due to anonymous review].</a></li>
</ol>

<h3>Conferences</h3>

<ol>
<li><a href="#">[C1] S. T. Ahmed, et al., Binary Bayesian Neural Networks for Efficient Uncertainty Estimation Leveraging Inherent Stochasticity of Spintronic Devices, IEEE/ACM International Symposium on Nanoscale Architectures (NANOARCH), 2022. [**Best Paper Candidate**. <details> <summary>Abstract:</summary>In the age of automation, machine learning systems for real-time critical decisions in various domains such as autonomous driving are at an all-time high. Predictive uncertainty allows a machine learning system to make more insightful decisions by avoiding blind predictions. Algorithmically, Bayesian neural networks (BayNNs) based on dropout are principled methods for estimating predictive uncertainty in a machine learning application. However, the computational cost and power consumption make the use of BayNNs on embedded hardware unattractive. Hardware accelerators with emerging non-volatile resistive memories (NVMs) such as Magnetic Tunnel Junction (MTJ) in conjunction with quantized models are an interesting option for efficient implementations of such a system. Binary BayNNs are a desirable alternative  that can provide predictive uncertainty efficiently by combining the benefits of quantization and hardware acceleration. In this paper, propose for the first time the binary bayesian neural network (BayBNN) using dropout-based approximation, and we leverage the inherent randomness of spintronic devices for in-memory Bayesian inference. Our proposed method can

