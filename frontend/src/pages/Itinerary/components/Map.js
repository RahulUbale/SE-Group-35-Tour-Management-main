import React from "react";

export const Map = () => {
  const handleOpenMap = () => {
    const latitude = 37.7749; // Replace with the latitude of your location
    const longitude = -122.4194; // Replace with the longitude of your location
    const zoom = 15; // Replace with the zoom level you want
    const markerLabel = "Taj Mahal"; // Replace with the label you want for the marker
    const url = `https://www.google.com/maps?q=${latitude},${longitude}&z=${zoom}&t=k&z=${zoom}&ie=UTF8&iwloc=&output=embed&hl=en&markers=${latitude},${longitude}&q=${latitude},${longitude}(${markerLabel})`;

    window.open(url, "_blank");
  };
  return (
    <div>
      <button onClick={handleOpenMap}>Open Map</button>
    </div>
  );
};
