using System;
using NUnit.Framework;
using WindroseOptimizer;

namespace WindroseOptimizer.Tests
{
    [TestFixture]
    public class WindroseTrainerTests
    {
        [Test]
        public void Train_ReturnsValidAngle()
        {
            var config = new TrainingConfig { Epochs = 50, LearningRate = 0.1 };
            var trainer = new WindroseTrainer(config);
            var result = trainer.Train();
            Assert.That(result.BestAngle, Is.InRange(0, 360));
            Assert.That(result.Score, Is.GreaterThan(0));
        }

        [Test]
        public void Train_WithOneEpoch_ReturnsSomeAngle()
        {
            var config = new TrainingConfig { Epochs = 1 };
            var trainer = new WindroseTrainer(config);
            var result = trainer.Train();
            Assert.That(result.BestAngle, Is.InRange(0, 360));
        }
    }
}