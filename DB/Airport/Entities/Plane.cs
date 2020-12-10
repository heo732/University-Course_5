﻿using System;
using System.Collections.Generic;

namespace Airport.Entities
{
    public class Plane
    {
        public int Id { get; set; }

        public string Number { get; set; }

        public int PlaneTypeId { get; set; }

        public PlaneType PlaneType { get; set; }

        public DateTime ManufactureDate { get; set; }

        public int SeatsNumber { get; set; }

        public int BrigadeId { get; set; }

        public Brigade Brigade { get; set; }

        public List<Flight> Flights { get; set; } = new List<Flight>();

        public List<Inspection> Inspections { get; set; } = new List<Inspection>();
    }
}