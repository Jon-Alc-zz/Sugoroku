class Main extends React.Component{
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

ReactDOM.render(
	<Main />,
	document.getElementById("container")
);