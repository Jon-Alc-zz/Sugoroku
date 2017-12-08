class AboutUs extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div>
				<h1>About Us</h1>
				<p>December 2017
					We made this site to help people learn about this obscure and underappreciated genre of analog games, which is an ongoing research field at UCSC. The generator was created for Game AI class at UCSC.
					This website is built with JavaScript and React.js, and the Board Generator is implemented using a variable-point crossover genetic algorithm in Python 3.6.
					We are UCSC undergraduates studying Computer Science and Game Design! Hire Us!
				</p>
				<p>
					Contact:
					Jon Alc
					Yuvi Dube
					Ryen Haimez
					Joreeena Lam
					Ryenuihong Yu
				</p>
			</div>
		);
	}
}