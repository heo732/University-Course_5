using System.Collections.Generic;

namespace Airport.Entities
{
    public class Brigade : BaseEntity
    {
        public List<Employee> Employees { get; set; } = new List<Employee>();

        public List<Plane> Planes { get; set; } = new List<Plane>();
    }
}