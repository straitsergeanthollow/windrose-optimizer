using System;
using System.IO;

namespace WindroseOptimizer
{
    class Program
    {
        static void Main(string[] args)
        {
            var config = ConfigLoader.Load("config.json");
            var trainer = new WindroseTrainer(config);
            var result = trainer.Train();
            Console.WriteLine($"Training complete. Best angle: {result.BestAngle}°, score: {result.Score:F2}");
            File.WriteAllText("output.json", result.ToJson());
        }
    }
}