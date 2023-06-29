import "./Itinerary.css";
import { TodoWrapper } from "./components/TodoWrapper";

import NavBar from '../../components/NavBar';

function Itinerary() {
  const numberOfCards = 5;
  return (
    <div className="Main">
      <NavBar/>
      {Array(numberOfCards)
        .fill()
        .map((_, index) => (
          <div key={index}>
            <h2>Day: {index + 1}</h2>
            <TodoWrapper key={index} />
          </div>
        ))}
    </div>
  );
}

export default Itinerary;
