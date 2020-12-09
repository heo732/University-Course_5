using System;
using System.Linq;

namespace Airport
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //using (var db = new Context())
            //{
            //    db.PlaneTypes.Add(new PlaneType { Value = "huge" });
            //    db.SaveChanges();
            //}

            using (var db = new Context())
            {
                var planeTypes = db.PlaneTypes.ToList();
            }
        }
    }
}