class Navbar extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div id="navbar">
				<div id="navTitle">双六・Sugoroku</div>

				<div id="navLinks">
					<div className="navButton">
						<IndexLink to="/" className="routerLink" activeClassName="active" className="link" id="home">Home</IndexLink>
					</div>
					<div className="navButton">
						<Link to="history" className="routerLink" activeClassName="active" className="link" id="history">History</Link>
					</div>
					<div className="navButton">
						<Link to="algorithm" className="routerLink" activeClassName="active" className="link" id="algorithm">Algorithm</Link>
					</div>
					<div className="navButton">
						<Link to="about" className="routerLink" activeClassName="active" className="link" id="about">About Us</Link>
					</div>
				</div>
			</div>
		);
	}
}