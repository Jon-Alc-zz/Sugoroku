class JSONParser extends React.Component{
	constructor(props){
		super(props);

		this.state = {
			title: "",
			author: "",
			dice: "",
			numSpaces: 0,
			spaceKeys: [],
            currentBoard:"--"
		};

		this.parser = this.parser.bind(this);
        this.showList = this.showList.bind(this);
        this.changeName = this.changeName.bind(this);
	}

    changeName(name, url){
        this.setState({
            currentBoard: name
        },()=>{
            this.parser(url);
        });
    }

	parser(url){
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

        xmlHttp.open("GET", url, true);
        xmlHttp.send(null);
	}

    showList(){
        document.getElementById("dropdownList").classList.toggle("show");
    }

	render(){
		return(
			<div id="sugorokuBoardButton">
                <div id="currentDropdown" onClick={this.showList}>
                    {this.state.currentBoard}

                    <i className="glyphicon glyphicon-menu-down dropdownIcon"></i>
                </div>

                <div id="dropdownList" className="dropdownContent">
                    <a href="#">--</a>
                    <a href="#" onClick={()=>this.changeName("Board 1", "Python-Sugoroku/Python-Sugoroku/input_board.json")}>
                        Board 1
                    </a>
                    <a href="#">Afrikaans</a>
                </div>
			</div>
		);
	}
}

window.onclick = function(event) {
    if (!event.target.matches('#currentDropdown')) {
        var dropdowns = document.getElementsByClassName("dropdownContent");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}