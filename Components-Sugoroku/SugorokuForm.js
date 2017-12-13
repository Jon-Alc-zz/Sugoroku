class SugorokuForm extends React.Component{
	constructor(props){
		super(props);

		this.state={
			firstName: "",
			lastName: "",
			callBackData:""
		}

		this.handleFirstName = this.handleFirstName.bind(this);
		this.handleLastName = this.handleLastName.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleFirstName(event){
		this.setState({
			firstName: event.target.value
		})
	}

	handleLastName(event){
		this.setState({
			lastName: event.target.value
		});
	}

	handleSubmit(event){
		$.ajax({
			type:"POST",
      		url: "../Python-Sugoroku/Python-Sugoroku/Sugoroku.py",
      		data:{
      			firstName:this.state.firstName,
      			lastName:this.state.lastName
      		},
      		cache: false,
      		success: function(data) {
        		this.setState({
        			callBackData: data
        		},()=>{
        			console.log(this.state.callBackData)
        		});
      		}.bind(this),
      		error: function(xhr, status, err) {
        		console.error("hi", status, err.toString());
      		}.bind(this)
    	});
	}

	render(){
		return(
			<form onSubmit={this.handleSubmit}>
			<label>
  				First name:
 				<input type="text" value={this.state.firstName} onChange={this.handleFirstName} />
 			</label>

 			<label>
  				Last name:
  				<input type="text" value={this.state.lastName} onChange={this.handleLastName} />
  			</label>

  			<input type="submit" value="Submit" />
  			</form>
		);
	}
}