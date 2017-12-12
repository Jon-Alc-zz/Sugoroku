class SugorokuHome extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			JSONFile: {},
			spaceKeysArr: []
		}

		this.setJSONFile = this.setJSONFile.bind(this);
		this.setSpaceKeys = this.setSpaceKeys.bind(this);
	}

	setJSONFile(info){
		this.setState({
			JSONFile: info
		});
	}

	setSpaceKeys(spaces){
		this.setState({
			spaceKeysArr: spaces
		});
	}

	render(){
		return(
			<div className="bodyText">
				<h1>About Sugoroku</h1>
				<div className="textBox">
					Sugoroku is a genre of board games with 10 or more tiles that connect to form a completed story.
					Players move around the board in 2 ways: along a designated path with dice rolls or to specific 
					squares following the instructions on the square they landed on. You can play these types of game 
					with as many people as you want. You can even play by yourself.
				</div>

				<h1>About this Site</h1>
				<div className="textBox">
					The purpose of this site is to ________________.
					These games are played with a 6 sided dice. 
					Click the button below to generate a unique Sugoroku board game.
				</div>

				<h1>Example Boards</h1>
					<JSONParser 
						setJSONFile={this.setJSONFile}
						setSpaceKeys={this.setSpaceKeys} />

				<div className="textBox">
				<BoardDisplay 
					getJSONFile={this.state.JSONFile}
					getSpaceKeys={this.state.spaceKeysArr} />
				</div>
			</div>
		);
	}
}