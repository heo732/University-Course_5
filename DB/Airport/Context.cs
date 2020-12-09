using Microsoft.EntityFrameworkCore;

namespace Airport
{
    public class Context : DbContext
    {
        public DbSet<PlaneType> PlaneTypes { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseOracle(@"User Id=SYS; Password=admin; DBA Privilege=SYSDBA; Data Source=192.168.88.238/xe;");
        }
    }
}