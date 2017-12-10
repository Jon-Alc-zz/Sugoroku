class AboutUs extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div className="bodyText">
				<h1>About Us</h1>
				<div className="textBox">December 2017
					We made this site to help people learn about this obscure and underappreciated genre of analog games, which is an ongoing research field at UCSC. The generator was created for Game AI class at UCSC.
					This website is built with JavaScript and React.js, and the Board Generator is implemented using a variable-point crossover genetic algorithm in Python 3.6.
					We are UCSC undergraduates studying Computer Science and Game Design! Hire Us!
				</div>

				<h1>Contact Us</h1>
				<div className="textBox">
					Jon Alc
					Yuvi Dube
					Ryen Haimez
					Joreeena Lam
					Ryenuihong Yu
				</div>
			</div>
		);
	}
}