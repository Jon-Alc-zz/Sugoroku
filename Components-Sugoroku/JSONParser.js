class JSONParser extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			title: "",
			author: "",
			dice: "",
			numSpaces: 0,
			spaceKeys: []
		};

		this.parser = this.parser.bind(this);
	}

	parser(){
		var xmlHttp = new XMLHttpRequest();

    	xmlHttp.onreadystatechange = function() { 
        	if (xmlHttp.readyState == 4){
        		var XMLResponse = JSON.parse(xmlHttp.responseText);
        		if(xmlHttp.status == 200){
        			this.setState({
        				title: XMLResponse.title,
        				author: XMLResponse.author,
        				dice: XMLResponse.dice,
        				numSpaces: Object.keys(XMLResponse.transitions).length
        			},()=>{
        				var tempKeys = []
        				for(var k in XMLResponse.transitions){
        					tempKeys.push(k);
        				}

        				this.setState({
        					spaceKeys: tempKeys
        				}, ()=>{
        					this.props.setJSONFile(XMLResponse);
        					this.props.setSpaceKeys(this.state.spaceKeys);
        				});
        			});

        		}else{
        			console.log("Can't parse");
        		}
        	}
        }.bind(this);

        xmlHttp.open("GET", "data/JonTestFile.json", true);
        xmlHttp.send(null);
	}

	render(){
		return(
			<div id="sugorokuBoardButton">
				<button onClick={this.parser}>Click Ryan</button>
			</div>
		);
	}
}