class Main extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<JSONParser />
		);
	}
}

ReactDOM.render(
	<Main />,
	document.getElementById("container")
);