using System;
using System.IO;
using System.Text.Json;

namespace WindroseOptimizer
{
    public class ConfigLoader
    {
        public static TrainingConfig Load(string path)
        {
            if (!File.Exists(path))
            {
                Console.WriteLine("Config not found, using defaults.");
                return new TrainingConfig { Epochs = 100, LearningRate = 0.01 };
            }
            var json = File.ReadAllText(path);
            return JsonSerializer.Deserialize<TrainingConfig>(json) ?? new TrainingConfig();
        }
    }

    public class TrainingConfig
    {
        public int Epochs { get; set; } = 100;
        public double LearningRate { get; set; } = 0.01;
    }
}