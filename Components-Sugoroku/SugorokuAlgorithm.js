class SugorokuAlgorithm extends React.Component{
	constructor(props){
		super(props);
	}

	render(){
		return(
			<div className="bodyText">
				<h1>Genetic Algorithm</h1>
				<div className="textBox">
                    <p>The algorithm uses fitness metrics for randomness, board length, desired average number of turns to solve board, preference for closed jumping boards(mazes), and preference for boards with long designated jumps(bridges).</p>

                    <p>Fitness scores are calculated by combining a score derived from the board elements and the average number of turns that two players with weighted rolls take to complete the board. Normal boards compare the board length and give scaling penalties the bigger the difference from the desired board length. They also give marginally decreasing rewards for each bonus random space based on the randomness input. For mazes, the simulated players have a slightly higher chance of rolling out of closed loops with an average of 3.33 on rolls. Individual smaller boards of the same type are generated with this algorithm and the most fit are paired to generate children with a slightly changed variable point crossover using ranked selection. The crossover prefers to use points closer to the middle of boards to avoid large board size growth that will skew fitness.</p>
                    <p>Mutation is done depending on the type of small board. Straight boards will sometimes change length, depending on the length multiplier variable. They also have a small chance of changing a normal space to a jump space and vice versa. Maze boards rearrange each space’s jump locations, and bridge boards vary the distance between the fall spaces and the space the fall would end up on. The combined boards have a preference to not put the same type of boards next to each other to encourage variety. The end result is a large board made with the most fit smaller boards.</p>
                    <h3>Solvability</h3>
                    <p>Each generated smaller board must be solvable since the fitness calculation depends on having an automated player play through the board. This is accomplished by starting with a solvable board and only modifying boards in such a way that they always end up being solvable.</p>
                    <p>Normal boards begin with start and end spaces that don’t have any effect, and two types of spaces are added in. The first type has no effect, and the second type has a chance to make the player jump forward or backwards. Since every space has a chance of behaving like an empty space, every board generated with this algorithm is guaranteed to be solvable. During reproduction, each board is made from a combination of solvable boards, so the generated boards are guaranteed to be solvable as well.</p>
                    <p>Maze boards are guaranteed to be solvable because there will always be one direct route from start to end. Rearranging these spaces with this condition will still always result in a solvable board.</p>
                    <p>Bridge boards are always solvable because the only jumps are forward.</p>
                    <h3>The Code</h3>
                    <p>Click <a href="https://github.com/Jon-Alc/Sugoroku">here</a> to go to our GitHub page.</p>
				</div>
			</div>
		);
	}
}