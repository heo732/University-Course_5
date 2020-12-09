using Airport.Entities;
using Microsoft.EntityFrameworkCore;

namespace Airport
{
    public class Context : DbContext
    {
        public DbSet<PlaneType> PlaneTypes { get; set; }

        public DbSet<FlightType> FlightTypes { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseOracle(@"User Id=SYS; Password=admin; DBA Privilege=SYSDBA; Data Source=localhost:1521/xe;");
        }
    }
}