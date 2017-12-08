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
			<div>
			<h1>About Sugoroku</h1>
				<p>
					Sugoroku is a genre of board games with 10 or more tiles that connect to form a completed story.
					Players move around the board in 2 ways: along a designated path with dice rolls or to specific squares following the instructions on the square they landed on. You can play these types of game with as many people as you want. You can even play by yourself.
					This site generates Sugoroku board games that are played with a 6 sided dice. Click the button below to generate a unique Sugoroku board game.
				</p>

				<BoardDisplay 
					getJSONFile={this.state.JSONFile}
					getSpaceKeys={this.state.spaceKeysArr} />

				<JSONParser 
					setJSONFile={this.setJSONFile}
					setSpaceKeys={this.setSpaceKeys} />
			</div>
		);
	}
}