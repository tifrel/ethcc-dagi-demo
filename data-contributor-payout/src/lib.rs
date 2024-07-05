use near_sdk::{
    env, near, serde_json::json, store::IterableMap, AccountId, NearToken, PanicOnDefault, Promise,
};

#[near(contract_state, serializers = [borsh])]
#[derive(PanicOnDefault)]
pub struct DataContributorPayout {
    // TODO: remove for presentation
    payouts_by_contributor: IterableMap<AccountId, NearToken>,
}

#[near]
impl DataContributorPayout {
    #[init]
    pub fn init() -> Self {
        Self {
            payouts_by_contributor: IterableMap::new(b"a"),
        }
    }

    pub fn contribute(&self, x: f64, y: f64) {
        env::log_str(
            json!({"x": x, "y": y, "contributor_id": env::predecessor_account_id()})
                .to_string()
                .as_str(),
        )
    }

    #[private]
    pub fn pay_contributor(&mut self, contributor_id: AccountId, amount: NearToken) -> Promise {
        self.payouts_by_contributor.remove(&contributor_id);
        Promise::new(contributor_id).transfer(amount)
    }

    pub fn get_payout_for_contributor(&self, contributor_id: AccountId) -> NearToken {
        self.payouts_by_contributor
            .get(&contributor_id)
            .cloned()
            .unwrap_or_default()
    }
}
