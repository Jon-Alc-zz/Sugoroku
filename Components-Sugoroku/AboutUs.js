class AboutUs extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div className="bodyText">
                <h1>About this Site</h1>
				<div className="textBox">
					The purpose of this site is to share the history of Sugoroku.
                    <div>The Sugoroku board game generator was built for the final project for our Game AI class.&nbsp;</div>
					This site was made to host our generator and to inform people about this obscure and underappreciated genre of analog games being researched at UCSC.
                    We were inspired by our mentor, Nathan Altice, who has been archiving Bandai board games from the 1980s and 90s. During his work, he noticed that many of the games were of the Sugoroku genre. <br></br>
					<div>This website is built with JavaScript and React.js, and the Board Generator is implemented using a variable-point crossover genetic algorithm in Python 3.6. &nbsp;</div>
				</div>
				<h1>About Us</h1>
				<div className="textBox">
					<div>We are UCSC undergraduates studying Computer Science and Game Design.</div>
                    <br></br>
					<div>
					Jonathan Alcantara - jonalcantara96@gmail.com
					</div>
                    <div>
					Yuvika Dube - yuvikadube@gmail.com
					</div>
                    <div>
					Ryan Jaime - ryanjjaime@gmail.com
					</div>
                    <div>
					Jolina Lam - joyelam@ucsc.edu
					</div>
                    <div>
					Ruihong Yu - ruyu@ucsc.edu
					</div>
				</div>
			</div>
		);
	}
}